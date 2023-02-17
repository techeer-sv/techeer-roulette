## About

테커 미팅에서 랜덤으로 사람을 뽑아주는 룰렛입니다.

## Run

먼저 candidates.txt에 룰렛에 당첨될 사람들의 이름을 줄 단위로 적습니다.

예:

```
홍길동
김철수
이영희
```

명단 중 한 명만 뽑고 싶을 땐 `single.py`를 실행합니다.

```bash
$ python3 single.py candidates.txt
```

명단에서 랜덤 순서로 발표자를 뽑고 싶으면 `sequential.py`를 실행합니다.

```bash
$ python3 sequential.py candidates.txt
```
