-module(main).
-compile(export_all).
-include_lib("eunit/include/eunit.hrl").


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



solve(Filename, Part2) ->
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

    {EndX, EndY} = EndPos,

    %% Add the outgoing edges for the east node of the given position:
    %% Note: Since we don't care in which direction you end up being oriented when you reach the goal square,
    %% We'll represent the goal square as a singe node: {X, Y, goal}.
    AddEdges = fun(X, Y, Dir, Map) ->
                       {Nx, Ny} = Delta(X, Y, Dir),
                       TurnEdges = [{{X, Y, maps:get(Dir, CCW)}, 1000},
                                    {{X, Y, maps:get(Dir, CW)}, 1000}],
                       CurChar = maps:get({X, Y}, Dict),
                       Edges = case maps:get({Nx, Ny}, Dict) of
                                   Ch when Ch =/= $# -> 
                                       if {Nx, Ny} == EndPos ->
                                               %% Don't split the goal square into 4 nodes
                                               TurnEdges ++ [{{Nx, Ny, goal}, 1}];
                                          true ->
                                               TurnEdges ++ [{{Nx, Ny, Dir}, 1}] 
                                       end;
                                   _ -> TurnEdges
                               end,
                       Node = case CurChar of $E -> {X, Y, goal}; _ -> {X, Y, Dir} end,
                       maps:put(Node, Edges, Map)
               end,

    G = lists:foldl(fun({{X, Y}, Ch}, AccMap) ->
                            if Ch == $# -> AccMap;
                               true -> lists:foldl(fun(Dir, Acc) -> AddEdges(X, Y, Dir, Acc) end,
                                                   AccMap, [e, w, n, s])
                            end
                    end,
                    #{}, 
                    Coords),
    
    Heuristic = fun({X, Y, _}) -> abs(X - EndX) + abs(Y - EndY) end,
    {StartX, StartY} = StartPos,
    StartNode = {StartX, StartY, e},

    case Part2 of
        false -> 
            {MinDist, Paths} = search:search(StartNode, {EndX, EndY, goal}, G, Heuristic),
            MinDist;
        true ->
            {MinDist, Paths} = search:search(StartNode, {EndX, EndY, goal}, G, Heuristic),
            VisitedNodes = sets:from_list(lists:map(fun({X, Y, _}) -> {X, Y} end, lists:flatten(Paths))),
            sets:size(VisitedNodes)
    end. 


part1_ex1_test() ->
    ?assertEqual(7036, solve("example1.txt", false)).

part1_ex2_test() ->
    ?assertEqual(11048, solve("example2.txt", false)).

part1_test() ->
    ?assertEqual(85432, solve("input.txt", false)).

part2_ex1_test() ->
    ?assertEqual(45, solve("example1.txt", true)).

part2_ex2_test() ->
    ?assertEqual(64, solve("example2.txt", true)).

part2_test() ->
    ?assertEqual(465, solve("input.txt", true)).
