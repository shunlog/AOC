-module(main).
-compile(export_all).


read(Filename) ->
    {ok, Binary} = file:read_file(Filename),
    binary_to_list(Binary).


solve1(Str) ->
    Result = re:run(Str, "mul\\((\\d+),(\\d+)\\)", [global, {capture,[1, 2],list}]),
    case Result of
        {match, Lls} -> 
            MultPair = fun([F, S]) -> list_to_integer(F) * list_to_integer(S) end,
            Terms = lists:map(MultPair, Lls),
            Sum = lists:foldl(fun(V, Acc) -> V + Acc end, 0, Terms),
            Sum;
        _ -> 0
    end.


solve2(Str) ->
    %% Concat all lines
    Str2 = re:replace(Str, "\\n", "", [global]),
    %% Remove all segments that are deactivated by the don't(),
    %% By removing all the matches of "don't()..." up to a "do()"
    Str3 = re:replace(Str2, "don't\\(\\).*?(?=do\\(\\)|$)", "", [global]),
    solve1(Str3).


test() ->
    Test = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)\n+mul(32,64]then(mul(11,8)mul(8,5))",
    solve1(Test),
    S1 = solve1(Test),
    io:format("~p~n", [S1]),
    
    Test2 = "xmul(2,4)&mul[3,7]!^don't()_\nmul(5,5)don't()+mul(32,64](mul(11,8)undo()?mul(8,5))",
    S2 = solve2(Test2),
    io:format("~p~n", [S2]).    


solve(Fn) ->
    S1 = solve1(read(Fn)),
    io:format("~p~n", [S1]),
    
    S2 = solve2(read(Fn)),
    io:format("~p~n", [S2]).    
    
