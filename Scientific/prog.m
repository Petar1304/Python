clear all;
close all;
clc;

N = 1000000;

a = 1;
b = 1;

for n = 1:N
  x = rand(1)*(-2) + 1;
  y = rand(1)*(-2) + 1;
  if x^2 + y^2 <= 1
    circleX(a) = x;
    circleY(a) = y;
    a = a + 1;
  else
    squareX(b) = x;
    squareY(b) = y;
    b = b + 1;
  end
end

PI = 4*(length(circleX) / N)

figure(1)
plot(squareX, squareY, 'r.')
hold all
plot(circleX, circleY, 'g.')
grid minor
