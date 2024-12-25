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
    {_, Node, Open2} = multi_gb_trees:take_smallest(Open),
    if Node =:= Goal ->
            Dist = maps:get(Goal, Fscores),
            Path = trace(Goal, CameFrom),
            {Dist, Path};
       true ->
            {NewOpen, NewG, NewF, NewCameFrom} = 
                update_neighbors(Node, Graph, Heuristic, Open2, Gscores, Fscores, CameFrom),
            search_loop(Goal, Graph, Heuristic, NewOpen, NewG, NewF, NewCameFrom)
    end.


search_all(Start, Goal, Graph, Heuristic) ->
    %% Like search, but returns a {Dist, [Path]} with a list of equally good paths.
    Empty = gb_trees:empty(),
    Open = multi_gb_trees:add(0, Start, Empty),
    search_loop(Goal, Graph, Heuristic,
                Open, #{Start => 0}, #{}, #{}).


search_all_loop(Goal, Graph, Heuristic, Open, Gscores, Fscores, CameFrom) ->
    %% instead of taking only one of the elements with the same key,
    %% call the function recursively for all of them and then append the results
    {_, Node, Open2} = multi_gb_trees:take_smallest(Open),
    if Node =:= Goal ->
            Dist = maps:get(Goal, Fscores),
            Path = trace(Goal, CameFrom),
            {Dist, Path};
       true ->
            {NewOpen, NewG, NewF, NewCameFrom} = 
                update_neighbors(Node, Graph, Heuristic, Open2, Gscores, Fscores, CameFrom),
            search_loop(Goal, Graph, Heuristic, NewOpen, NewG, NewF, NewCameFrom)
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
    if Tentative_Gscore >= Neighbor_Gscore ->
            %% Found a worse path to node, do nothing
            update_neighbors_loop(Rest, Node, Heuristic,
                                  Open, Gscores, Fscores, CameFrom);
       true ->
            %% Found a better path to node
            NewCameFrom = CameFrom#{Neighbor => Node},
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
        nil -> [Node | Path];
        PrevNode -> trace(Goal, CameFrom, PrevNode, [Node | Path])
    end.

                      
trace_path_test() ->
    ?assertEqual([a, b], trace(b, #{b => a})),
    CameFrom = #{c => a,f => b,b => a,d => c,e => d,z => e},
    ?assertEqual([a, c, d, e, z], trace(z, CameFrom)).


search_basecase_test() ->
    G = #{a => [{z, 1}]},
    H = #{a => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, Path} = search(a, z, G, Heuristic),
    ?assertEqual(1, Dist),
    ?assertEqual([a, z], Path).


search_basecase2_test() ->
    G = #{a => [{b, 1}],
          b => [{z, 1}]},
    H = #{a => 2, b => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, Path} = search(a, z, G, Heuristic),
    ?assertEqual(2, Dist),
    ?assertEqual([a, b, z], Path).


search_all_basecase_test() ->
    G = #{a => [{b, 1}, {c, 2}],
          b => [{z, 2}],
          c => [{z, 1}]},
    H = #{a => 1, b => 2, c=> 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, [Path1, Path2]} = search_all(a, z, G, Heuristic),
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
    {Dist, Path} = search(a, z, G, Heuristic),
    ?assertEqual(2, Dist),
    ?assertEqual([a, b, z], Path).


search_with_tuples_for_nodes_test() ->
    {A, B, Z} = {{1, 0}, {1, 1}, {1, 2}},
    G = #{A => [{B, 1}] ,
          B => [{Z, 1}]},
    H = #{A => 2, B => 1, Z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    {Dist, Path} = search(A, Z, G, Heuristic),
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
    {Dist, Path} = search(a, z, G, Heuristic),
    ?assertEqual(17, Dist),
    ?assertEqual([a, c, d, e, z], Path).
