-module(window).
-include_lib("eunit/include/eunit.hrl").
-export([window/2]).

window(L, N) when length(L) =< N -> [L];
window(L, N) -> 
    [lists:sublist(L, N) | window(tl(L), N)].

window_test() ->
    ?assertEqual([[1, 2], [2, 3]], window([1, 2, 3], 2)),
    ?assertEqual([[1], [2], [3]], window([1, 2, 3], 1)),
    ?assertEqual([[1, 2, 3]], window([1, 2, 3], 3)),
    %% simply return the list on overflow
    ?assertEqual([[1, 2, 3]], window([1, 2, 3], 4)).
