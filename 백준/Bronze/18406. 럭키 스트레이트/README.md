# [Bronze II] 럭키 스트레이트 - 18406 

[문제 링크](https://www.acmicpc.net/problem/18406) 

### 성능 요약

메모리: 1112 KB, 시간: 0 ms

### 분류

구현, 문자열

### 제출 일자

2025년 6월 16일 17:22:06

### 문제 설명

<p>어떤 게임의 아웃복서 캐릭터에게는 럭키 스트레이트라는 기술이 존재한다. 이 기술은 매우 강력한 대신에 항상 사용할 수는 없으며, 현재 게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있다.</p>

<p>특정 조건이란 현재 캐릭터의 점수를 <em>N</em>이라고 할 때 점수 <em>N</em>을 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황을 의미한다. 예를 들어 현재 점수가 123,402라면 왼쪽 부분의 각 자릿수의 합은 1+2+3, 오른쪽 부분의 각 자릿수의 합은 4+0+2이므로 두 합이 6으로 동일하여 럭키 스트레이트를 사용할 수 있다.</p>

<p>현재 점수 <em>N</em>이 주어졌을 때, 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램을 작성하시오. 럭키 스트레이트를 사용할 수 있다면 "<code>LUCKY</code>"를, 사용할 수 없다면 "<code>READY</code>"라는 단어를 출력한다. 또한 점수 <em>N</em>의 자릿수는 항상 짝수 형태로만 주어진다. 예를 들어 자릿수가 5인 12,345와 같은 수는 입력으로 들어오지 않는다.</p>

### 입력 

 <p>첫째 줄에 점수 <em>N</em>이 정수로 주어진다. (10 ≤ <em>N</em> ≤ 99,999,999) 단, 점수 <em>N</em>의 자릿수는 항상 짝수 형태로만 주어진다.</p>

### 출력 

 <p>첫째 줄에 럭키 스트레이트를 사용할 수 있다면 "<code>LUCKY</code>"를, 사용할 수 없다면 "<code>READY</code>"라는 단어를 출력한다.</p>

