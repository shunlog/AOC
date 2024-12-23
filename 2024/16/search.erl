-module(search).
-compile(export_all).
-include_lib("eunit/include/eunit.hrl").

search(Start, Goal, Graph, Heuristic) ->
    %% Open is a balanced tree, where the nodes are key-value pairs
    %% where key = fScore, value = Node
    Empty = gb_trees:empty(),
    Open = multi_gb_trees:add(0, Start, Empty),
    search_loop(Goal, Open, #{Start => 0}, #{}, Graph, Heuristic).


search_loop(Goal, Open, Gscores, Fscores, Graph, Heuristic) ->
    {_, Node, NewOpen} = multi_gb_trees:take_smallest(Open),
    if Node =:= Goal ->
            maps:get(Goal, Fscores);
       true ->
            {NewOpen2, NewG, NewF} = update_neighbors(Node, Graph, Heuristic, NewOpen, Gscores, Fscores),
            search_loop(Goal, NewOpen2, NewG, NewF, Graph, Heuristic)
    end.


update_neighbors(Node, Graph, Heuristic, Open, Gscores, Fscores) ->
    NeighborsCosts = maps:get(Node, Graph),
    CurrentG = maps:get(Node, Gscores),
    update_neighbors_loop(NeighborsCosts, CurrentG, Heuristic, Open, Gscores, Fscores).


update_neighbors_loop([], _, _, Open, Gscores, Fscores) ->
    {Open, Gscores, Fscores};

update_neighbors_loop([{Neighbor, Cost} | Rest], CurrentG, Heuristic, Open, Gscores, Fscores) ->
    Tentative_Gscore = CurrentG + Cost,
    Neighbor_Gscore = maps:get(Neighbor, Gscores, 16#FFFFFFFFFFFFF),
    if Tentative_Gscore >= Neighbor_Gscore ->
            %% Found a worse path to node, do nothing
            update_neighbors_loop(Rest, CurrentG, Heuristic,
                                  Open, Gscores, Fscores);
       true ->
            %% Found a better path to node
            NewGscores = Gscores#{Neighbor => Tentative_Gscore},
            H = Heuristic(Neighbor),
            Fscore = Tentative_Gscore + H,
            NewFscores = Fscores#{Neighbor => Fscore},
            NewOpen = multi_gb_trees:add(Fscore, Neighbor, Open),
            update_neighbors_loop(Rest, CurrentG, Heuristic,
                                  NewOpen, NewGscores, NewFscores)
    end.
                                                   


search_basecase_test() ->
    G = #{a => [{z, 1}]},
    H = #{a => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    1 = search(a, z, G, Heuristic).


search_basecase2_test() ->
    G = #{a => [{b, 1}],
          b => [{z, 1}]},
    H = #{a => 2, b => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    2 = search(a, z, G, Heuristic).


search_backwards_edges_test() ->
    %% Had a bug because the update_neighbors_loop was terminating where it should've continued
    %% Add an edge from b back to a to test for this.
    G = #{a => [{b, 1}],
          b => [{a, 1}, {z, 1}]},
    H = #{a => 2, b => 1, z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    2 = search(a, z, G, Heuristic).


search_with_tuples_for_nodes_test() ->
    {A, B, Z} = {{1, 0}, {1, 1}, {1, 2}},
    G = #{A => [{B, 1}] ,
          B => [{Z, 1}]},
    H = #{A => 2, B => 1, Z => 0},
    Heuristic = fun(N) -> maps:get(N, H) end,
    2 = search(A, Z, G, Heuristic).


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

    17 = search(a, z, G, Heuristic).
