-module(main).
-compile(export_all).
-include_lib("eunit/include/eunit.hrl").


%% Take 1 element from each of the first N lists in M,
%% Return the formed list and the modified M

scoop(M, 0) ->
    {[], M};

scoop([L | R], N) when N > 0 ->
    V = hd(L),
    {Lscoop, NewR} = scoop(R, N-1),
    NewM = if length(L) > 1 -> [tl(L) | NewR];
              true -> NewR
           end,
    {[V | Lscoop], NewM}.


scoop_test() ->
    M = [[b3],
         [c2, c3],
         [d1, d2, d3]],    
    ?assertEqual({[b3], [[c2, c3], [d1, d2, d3]]}, scoop(M, 1)),
    ?assertEqual({[b3, c2], [[c3], [d1, d2, d3]]}, scoop(M, 2)),
    ?assertEqual({[b3, c2, d1], [[c3], [d2, d3]]}, scoop(M, 3)).
    

%% Given a matrix, return a list of diagonals
diags(M) -> diag(M, 1).

diag([[V]], 1) -> [[V]];
diag(M, N) ->
    {Lscoop, NewM} = scoop(M, N),    
    %% if the first row was exhausted, the next diagonal will have the same length
    NewN = if length(NewM) < length(M) -> N;
              %% otherwise it will be longer by 1
              true -> N + 1
           end,
    %% we can't scoop more than there are rows, so limit N to # of rows
    LimN = min(length(NewM), NewN),
    [Lscoop | diag(NewM, LimN)].


diag_test() ->
    ?assertEqual([[a]], diags([[a]])),

    M1 = [[a1, a2, a3],
          [b1, b2, b3]],
    ?assertEqual([[a1], [a2, b1], [a3, b2], [b3]], diags(M1)),

    M = [[a1, a2, a3],
         [b1, b2, b3],
         [c1, c2, c3],
         [d1, d2, d3]],
    Expected = [[a1],
                [a2, b1],
                [a3, b2, c1],
                [b3, c2, d1],
                [c3, d2], 
                [d3]],
    ?assertEqual(Expected, diag(M, 1)).


solve(Fn) ->
    {ok, Bin} = file:read_file(Fn),
    Bl = binary:split(Bin, <<"\n">>, [global, trim]),
    M = lists:map(fun binary_to_list/1, Bl),

    %% Given a line string, return # of matches
    CountLine = fun(Line) ->
                     lists:sum(lists:map(fun(L) -> 
                                                 if L == "XMAS"; L == "SAMX" -> 1; 
                                                    true -> 0 end
                                         end,
                                         window:window(Line, 4)))
             end,
    
    Horiz = lists:sum(lists:map(CountLine, M)),
    Vert = lists:sum(lists:map(CountLine, matrix:transpose(M))),
    Diag1 = lists:sum(lists:map(CountLine, diags(M))),
    Diag2 = lists:sum(lists:map(CountLine, diags(matrix:rot_ccw(M)))),
    Horiz + Vert + Diag1 + Diag2.

solve_ex1_test() ->
    ?assertEqual(18, solve("example1.txt")).

solve_input_test() ->
    ?assertEqual(2358, solve("input.txt")).
