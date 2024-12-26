-module(search).
-compile(export_all).
-include_lib("eunit/include/eunit.hrl").

search(Start, Goal, Graph, Heuristic) ->
    %% Open is a balanced tree, where the nodes are key-value pairs
    %% where key = fScore, value = Node
    Empty = gb_trees:empty(),
    Open = multi_gb_trees:add(0, Start, Empty),
    search_loop(Goal, Graph, Heuristic,
                Open, #{Start => 0}, #{}, #{}).


search_loop(Goal, Graph, Heuristic, Open, Gscores, Fscores, CameFrom) ->
    case multi_gb_trees:take_smallest(Open) of 
        {_, Node, Open2} ->
            if Node =:= Goal ->
                    Dist = maps:get(Goal, Gscores),
                    {NextFscore, _} = multi_gb_trees:smallest(Open2),
                    %% if the next potential path is definitely worse than the best found one 
                    %% there are no more alternative best paths
                    %% (guaranteed if the heuristic function never overestimates)
                    if NextFscore == error orelse NextFscore > Dist ->
                            Path = trace(Goal, CameFrom),
                            {Dist, Path};
                       true -> %% otherwise, continue looking at alternative paths
                            search_loop(Goal, Graph, Heuristic, Open2, Gscores, Fscores, CameFrom)
                    end;
               true ->
                    {NewOpen, NewG, NewF, NewCameFrom} = 
                        update_neighbors(Node, Graph, Heuristic, Open2, Gscores, Fscores, CameFrom),
                    search_loop(Goal, Graph, Heuristic, NewOpen, NewG, NewF, NewCameFrom)
            end;
        {error, _} ->                     
            Dist = maps:get(Goal, Gscores),
            Path = trace(Goal, CameFrom),
            {Dist, Path}

    end.



update_neighbors(Node, Graph, Heuristic, Open, Gscores, Fscores, CameFrom) ->
    NeighborsCosts = maps:get(Node, Graph),
    update_neighbors_loop(NeighborsCosts, Node, Heuristic, Open, Gscores, Fscores, CameFrom).


update_neighbors_loop([], _, _, Open, Gscores, Fscores, CameFrom) ->
    {Open, Gscores, Fscores, CameFrom};

update_neighbors_loop([{Neighbor, Cost} | Rest], Node, Heuristic, Open, Gscores, Fscores, CameFrom) ->
    CurrentG = maps:get(Node, Gscores),
    Tentative_Gscore = CurrentG + Cost,
    Neighbor_Gscore = maps:get(Neighbor, Gscores, 16#FFFFFFFFFFFFF),
    if Tentative_Gscore > Neighbor_Gscore ->
            %% Found a worse path to node, do nothing
            update_neighbors_loop(Rest, Node, Heuristic,
                                  Open, Gscores, Fscores, CameFrom);
       true ->
            %% Found a better or equally good path to node
            NewCameFrom = if Tentative_Gscore < Neighbor_Gscore ->
                                  CameFrom#{Neighbor => sets:from_list([Node])};
                             %% equally good path
                             Tentative_Gscore == Neighbor_Gscore -> 
                                  Set = maps:get(Neighbor, CameFrom, sets:new()),
                                  CameFrom#{Neighbor => sets:add_element(Node, Set)}
                          end,
            NewGscores = Gscores#{Neighbor => Tentative_Gscore},
            H = Heuristic(Neighbor),
            Fscore = Tentative_Gscore + H,
            NewFscores = Fscores#{Neighbor => Fscore},
            NewOpen = multi_gb_trees:add(Fscore, Neighbor, Open),
            update_neighbors_loop(Rest, Node, Heuristic,
                                  NewOpen, NewGscores, NewFscores, NewCameFrom)
    end.
                         

trace(Goal, CameFrom) ->
    trace(Goal, CameFrom, Goal, []).

trace(Goal, CameFrom, Node, Path) ->
    case maps:get(Node, CameFrom, nil) of
        nil -> [[Node | Path]];
        NodesSet -> lists:foldl(
                      fun(L, Acc) -> Acc ++ L end,
                      [],
                      lists:map(fun(PrevNode) -> trace(Goal, CameFrom, PrevNode, [Node | Path]) end,
                                 sets:to_list(NodesSet)))
    end.

                      
trace_path_test() ->
    ?assertEqual([[a, b]], trace(b, #{b => sets:from_list([a])})),
    CameFromLists = #{c => [a],f => [b],b => [a],d => [c],e => [d],z => [e]},
    CameFrom = maps:map(fun(K, V) -> sets:from_list(V) end, CameFromLists),
    ?assertEqual([[a, c, d, e, z]], trace(z, CameFrom)).

                     
trace_multiple_test() ->
    CameFromLists = #{z => [c, b], b => [a, d], d => [a], c => [a]},
    CameFrom = maps:map(fun(K, V) -> sets:from_list(V) end, CameFromLists),
    Paths = trace(z, CameFrom),
    ?assertEqual(3, length(Paths)),
    ?assert(lists:member([a, d, b, z], Paths)),
    ?assert(lists:member([a, b, z], Paths)),
    ?assert(lists:member([a, c, z], Paths)).
    


search_basecase_test() ->
    G = #{a => [{z, 1}]},
    H = #{a => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path]} = search(a, z, G, Heuristic),
    ?assertEqual(1, Dist),
    ?assertEqual([a, z], Path).


search_basecase2_test() ->
    G = #{a => [{b, 1}],
          b => [{z, 1}]},
    H = #{a => 2, b => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path]} = search(a, z, G, Heuristic),
    ?assertEqual(2, Dist),
    ?assertEqual([a, b, z], Path).


search_all_basecase_test() ->
    G = #{a => [{b, 1}, {c, 2}],
          b => [{z, 2}],
          c => [{z, 1}]},
    H = #{a => 1, b => 2, c=> 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path1, Path2]} = search(a, z, G, Heuristic),
    ?assertEqual(3, Dist),
    ExpectedPaths = [[a, b, z], [a, c, z]],
    ?assert(lists:member(Path1, ExpectedPaths)),
    ?assert(lists:member(Path2, ExpectedPaths)).


search_all_2_test() ->
    %% add a third path [a, d, z]
    %% wchih will be explored because the heuristic for D will be too optimistic
    %% but shouldn't appear in the results because it's longer
    G = #{a => [{b, 1}, {c, 2}, {d, 2}],
          b => [{z, 2}],
          c => [{z, 1}],
          d => [{z, 2}]},
    H = #{a => 1, b => 2, c=> 1, d => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path1, Path2]} = search(a, z, G, Heuristic),
    ?assertEqual(3, Dist),
    ExpectedPaths = [[a, b, z], [a, c, z]],
    ?assert(lists:member(Path1, ExpectedPaths)),
    ?assert(lists:member(Path2, ExpectedPaths)).


search_backwards_edges_test() ->
    %% Had a bug because the update_neighbors_loop was terminating where it should've continued
    %% Add an edge from b back to a to test for this.
    G = #{a => [{b, 1}],
          b => [{a, 1}, {z, 1}]},
    H = #{a => 2, b => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path]} = search(a, z, G, Heuristic),
    ?assertEqual(2, Dist),
    ?assertEqual([a, b, z], Path).


search_with_tuples_for_nodes_test() ->
    {A, B, Z} = {{1, 0}, {1, 1}, {1, 2}},
    G = #{A => [{B, 1}] ,
          B => [{Z, 1}]},
    H = #{A => 2, B => 1, Z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path]} = search(A, Z, G, Heuristic),
    ?assertEqual(2, Dist),
    ?assertEqual([A, B, Z], Path).


search_big_test() ->
    G = #{
          a => [{b, 4}, {c, 3}],
          b => [{f, 5}, {e, 12}],
          c => [{e, 10}, {d, 7}],
          d => [{e, 2}],
          e => [{z, 5}],
          f => [{z, 15}]
         },

    H = #{
          a => 14,
          b => 12,
          c => 11,
          d => 6,
          e => 4,
          f => 11,
          z => 0
         },
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path]} = search(a, z, G, Heuristic),
    ?assertEqual(17, Dist),
    ?assertEqual([a, c, d, e, z], Path).
