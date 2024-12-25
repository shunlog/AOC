-module(main).
-compile(export_all).



read_file_as_list(Filename) ->
    {ok, IoDevice} = file:open(Filename, [read]),
    Lines = read_lines(IoDevice, []),
    file:close(IoDevice),
    Lines.

read_lines(IoDevice, Acc) ->
    case io:get_line(IoDevice, "") of
        eof -> lists:reverse(Acc);  % Reverse to maintain original order
        Line -> read_lines(IoDevice, [string:trim(Line) | Acc])  % Trim trailing newlines
    end.



solve(Filename) ->
    Lines = read_file_as_list(Filename),
    %% Extract list of tuples {X, Y, Character}
    Coords = lists:flatmap(fun({Y, Str}) -> 
                                   lists:map(
                                     fun({X, Ch}) -> {{X, Y}, Ch} end,
                                     lists:enumerate(Str)) 
                           end, 
                           lists:enumerate(Lines)),
    [{StartPos, _}] = lists:filter(fun({{_, _}, Ch}) -> Ch == $S end, Coords),
    [{EndPos, _}] = lists:filter(fun({{_, _}, Ch}) -> Ch == $E end, Coords),
    Dict = maps:from_list(Coords),

    CW = #{e => s, s => w, w => n, n => e},
    CCW = #{e => n, n => w, w => s, s => e},
    Delta = fun(X, Y, Dir) -> case Dir of
                                  e -> {X+1, Y};
                                  w -> {X-1, Y};
                                  s -> {X, Y+1};
                                  n -> {X, Y-1}
                              end
            end,

    %% Add the outgoing edges for the east node of the given position
    AddEdges = fun(X, Y, Dir, Map) ->
                       {Nx, Ny} = Delta(X, Y, Dir),
                       TurnEdges = [{{X, Y, maps:get(Dir, CCW)}, 1000},
                                    {{X, Y, maps:get(Dir, CW)}, 1000}],
                       Edges = case maps:get({Nx, Ny}, Dict) of
                                   Ch when Ch =/= $# -> 
                                       TurnEdges ++ [{{Nx, Ny, Dir}, 1}];
                                   _ -> TurnEdges
                               end,
                       maps:put({X, Y, Dir}, Edges, Map)
               end,

    G = lists:foldl(fun({{X, Y}, Ch}, AccMap) ->
                            if Ch == $# -> AccMap;
                               true -> lists:foldl(fun(Dir, Acc) -> AddEdges(X, Y, Dir, Acc) end,
                                                   AccMap, [e, w, n, s])
                            end
                    end,
                    #{}, 
                    Coords),

    {EndX, EndY} = EndPos,
    Heuristic = fun({X, Y, _}) -> abs(X - EndX) + abs(Y - EndY) end,

    {StartX, StartY} = StartPos,
    Solve = fun(Dir) -> search:search({StartX, StartY, e}, {EndX, EndY, Dir}, G, Heuristic) end,
    Sol = lists:min(lists:map(Solve, [e, w, n, s])),
    Sol.


part1_test() ->
    85432 = solve("input.txt").
