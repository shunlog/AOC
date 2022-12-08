##
# Project Title
#
# @file
# @version 0.1

main: main.cpp
	g++ -Wall -fdiagnostics-color -g main.cpp -o main

run: main
	./main

game: game.cpp matrix.cpp
	g++ -Wall -fdiagnostics-color matrix.cpp game.cpp -o game -lncurses

play: game
	./game

# end
