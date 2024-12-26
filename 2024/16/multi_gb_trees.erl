-module(multi_gb_trees).
-export([add/3, take/2, take_smallest/1, smallest/1]).
-include_lib("eunit/include/eunit.hrl").


%% Add a value to the list for a given key
add(Key, Value, Tree) ->
    case gb_trees:is_defined(Key, Tree) of
        true ->
            {OldList, NewTree} = gb_trees:take(Key, Tree),
            gb_trees:insert(Key, [Value | OldList], NewTree);
        false ->
            gb_trees:insert(Key, [Value], Tree)
    end.

%% Take a value from the list for a given key
take(Key, Tree) ->
    case gb_trees:is_defined(Key, Tree) of
        true ->
            {[Value | Rest], Tree2} = gb_trees:take(Key, Tree),
            NewTree = case Rest of
                          [] -> Tree2;  %% do nothing
                          _ -> gb_trees:insert(Key, Rest, Tree2)  %% Insert the other values back
                      end,
            {Value, NewTree};
        false ->
            {error, key_not_found}
    end.

%% Take the smallest key and remove it
take_smallest(Tree) ->
    case gb_trees:is_empty(Tree) of
        false ->
            {Key, Values} = gb_trees:smallest(Tree),
            [Value | Rest] = Values,
            NewTree = case Rest of
                          [] -> gb_trees:delete(Key, Tree); % Remove the key if no more values exist
                          _ -> gb_trees:enter(Key, Rest, Tree)  % Otherwise put back the rest
                      end,
            {Key, Value, NewTree};
        true ->
            {error, empty_tree}
    end.


%% Take the smallest key and remove it
smallest(Tree) ->
    case gb_trees:is_empty(Tree) of
        true-> {error, empty_tree};
        false ->
            {Key, [Value | _]} = gb_trees:smallest(Tree),
            {Key, Value}
    end.


%% Test adding values
add_values_test() ->
    Tree = gb_trees:empty(),
    Tree1 = add(1, a, Tree),
    Tree2 = add(1, b, Tree1),
    ?assertEqual([{1, [b, a]}], gb_trees:to_list(Tree2)).

%% Test taking a value
take_value_test() ->
    Tree = gb_trees:empty(),
    Tree1 = add(1, a, Tree),
    Tree2 = add(1, b, Tree1),
    {Value, Tree3} = take(1, Tree2),
    {RestValue, _} = take(1, Tree3),
    ?assert(lists:member(Value, [a, b])),
    ?assertEqual([{1, [RestValue]}], gb_trees:to_list(Tree3)),
    ?assert(lists:member(RestValue, [a, b])).

%% Test taking from a key with no values
take_from_empty_key_test() ->
    Tree = gb_trees:empty(),
    ?assertMatch({error, key_not_found}, take(1, Tree)).

%% Test adding and removing all values for a key
add_and_remove_all_test() ->
    Tree = gb_trees:empty(),
    Tree1 = add(1, a, Tree),
    Tree2 = add(1, b, Tree1),
    {_, Tree3} = take(1, Tree2),
    {_, Tree4} = take(1, Tree3),
    ?assertEqual([], gb_trees:to_list(Tree4)).


%% Test taking the smallest key
take_smallest_test() ->
    Tree = gb_trees:empty(),
    Tree1 = add(1, a, Tree),
    Tree2 = add(2, b, Tree1),
    Tree3 = add(3, c, Tree2),
    Tree4 = add(1, z, Tree3),
    {Key, Value, Tree5} = take_smallest(Tree4),
    ?assertEqual(1, Key),
    ?assert(lists:member(Value, [a, z])),
    {_, Value2, Tree6} = take_smallest(Tree5),
    ?assert(lists:member(Value2, [a, z])),
    ?assertEqual([{2, [b]}, {3, [c]}], gb_trees:to_list(Tree6)).


%% Test reading the smallest key
smallest_test() ->
    Tree = gb_trees:empty(),
    Tree1 = add(1, a, Tree),
    Tree2 = add(2, b, Tree1),
    Tree3 = add(3, c, Tree2),
    Tree4 = add(1, z, Tree3),
    {Key, Value} = smallest(Tree4),
    ?assertEqual(1, Key),
    ?assert(lists:member(Value, [a, z])).
