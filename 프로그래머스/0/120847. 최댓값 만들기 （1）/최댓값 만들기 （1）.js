function solution(numbers) {
    n = numbers.sort((a, b) => b - a);
    return numbers[0] * numbers[1];
}