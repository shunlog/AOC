-module(matrix).
-include_lib("eunit/include/eunit.hrl").
-export([transpose/1, rot_ccw/1]).


transpose([[]|_]) -> [];
transpose(M) ->
  [lists:map(fun hd/1, M) | transpose(lists:map(fun tl/1, M))].

transpose_test() ->
    M = [[a1,a2,a3],[b1,b2,b3],[c1,c2,c3]],
    Expected = [[a1,b1,c1],[a2,b2,c2],[a3,b3,c3]],
    ?assertEqual(Expected, transpose(M)).


rot_ccw(Matrix) ->
    Transposed = transpose(Matrix),
    lists:reverse(Transposed).
