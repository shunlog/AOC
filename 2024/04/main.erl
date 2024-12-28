-module(main).
-compile(export_all).
-include_lib("eunit/include/eunit.hrl").

window(L, N) when length(L) =< N -> [L];
window(L, N) -> 
    [lists:sublist(L, N) | window(tl(L), N)].

window_test() ->
    ?assertEqual([[1, 2], [2, 3]], window([1, 2, 3], 2)),
    ?assertEqual([[1], [2], [3]], window([1, 2, 3], 1)),
    ?assertEqual([[1, 2, 3]], window([1, 2, 3], 3)),
    %% simply return the list on overflow
    ?assertEqual([[1, 2, 3]], window([1, 2, 3], 4)).


transpose([[]|_]) -> [];
transpose(M) ->
  [lists:map(fun hd/1, M) | transpose(lists:map(fun tl/1, M))].

transpose_test() ->
    M = [[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]],
    Expected = [[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]],
    ?assertEqual(Expected, transpose(M)).



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
    

diag([[V]], 1) -> [[V]];

%% diag([[V | Rest]], 1) -> [[V] | diag(Rest, 1)];

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

diags(M) -> diag(M, 1).

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


%% diag_testing() ->
%%     M = [[a1, a2, a3],
%%          [b1, b2, b3],
%%          [c1, c2, c3],
%%          [d1, d2, d3]],
%%     M2 = [[a2, a3],
%%           [b1, b2, b3],
%%           [c1, c2, c3],
%%           [d1, d2, d3]],
%%     %% N increases
%%     diag(M, 1) = [a1] ++ diag(M2, 2),
%%     M3 = [[a3],
%%           [b2, b3],
%%           [c1, c2, c3],
%%           [d1, d2, d3]],
%%     diag(M3, 2) = [b1, a2] ++ diag(M3, 3),
%%     M4 = [[b3],
%%           [c2, c3],
%%           [d1, d2, d3]],
%%     %% N stays the same when first list is exhausted
%%     diag(M4, 3) = [c1, b2, a3] ++ diag(M5, 3),

%%     M5 = [[c3],
%%           [d2, d3]],
%%     %% N is limited to the number of remaining rows
%%     diag(M5, 2) = [d1, c2, b3] ++ diag(M6, 2).

    
rotl(Matrix) ->
    Transposed = transpose(Matrix),
    lists:reverse(Transposed).


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
                                         window(Line, 4)))
             end,
    
    Horiz = lists:sum(lists:map(CountLine, M)),
    Vert = lists:sum(lists:map(CountLine, transpose(M))),
    Diag1 = lists:sum(lists:map(CountLine, diags(M))),
    Diag2 = lists:sum(lists:map(CountLine, diags(rotl(M)))),
    Horiz + Vert + Diag1 + Diag2.
