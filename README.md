# Recipe Table Remake: DRF
[이 프로젝트](https://github.com/lemon-lime-honey/recipes-share-site)의 일부를 DRF로 구현한 프로젝트<br>
회원가입, 회원정보 수정, 회원탈퇴, 레시피 등록/수정/삭제, 레시피 후기 작성을 구현했다.

## 1. Project Structure
```
recipe-remake
 ┣ accounts
 ┃ ┣ models.py
 ┃ ┣ serializers.py
 ┃ ┣ urls.py
 ┃ ┗ views.py
 ┣ cfg
 ┃ ┣ permissions.py
 ┃ ┣ settings.py
 ┃ ┗ urls.py
 ┣ recipes
 ┃ ┣ models.py
 ┃ ┣ serializers.py
 ┃ ┣ urls.py
 ┃ ┗ views.py
 ┗ .env
```

- accounts: 사용자 계정에 관한 앱
- cfg: 프로젝트 설정 및 URL 구성
    - permissions.py: 프로젝트 전체에 해당하는 기본 권한 클래스
- recipes: 레시피에 관한 앱
- .env: 환경변수 집합
    - `secret_key`: Django SECRET KEY
    - `db_name`: 데이터베이스 이름
    - `db_user`: 계정명
    - `db_pw`: 비밀번호
    - `db_host`: 호스트 주소
    - `db_port`: 포트 번호

## 2. 개발 환경 구축
1. 다음을 실행하여 가상환경을 생성하고 필요한 패키지를 설치한다.
```bash
$ python -m venv venv
$ pip install -r requirements.txt
```

2. `MySQL`에서 다음을 실행한다. 이때 `db_name`은 `.env`에서 설명한 데이터베이스 이름이다.
```SQL
CREATE DATABASE `db_name`;
```

3. 가상환경을 활성화한 후 프로젝트 메인 디렉토리에서 다음을 실행한다.
```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

4. (선택) 관리자 계정을 생성한다.
```bash
$ python manage.py createsuperuser
```

## 3. API 엔드포인트 목록
### accounts

<details>
<summary> 가입 <code>POST</code> /accounts/signup/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| username | String | 아이디 |
| email | String | 이메일 |
| nickname | String | 닉네임 |
| birthdate | Date | 생년월일 |
| password | String | 비밀번호 |

- Response
    - `201 CREATED`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
        - 필드에 유효하지 않은 값을 입력한 경우
        - 아이디, 이메일, 닉네임이 중복된 경우

</details>

<details>
<summary> 로그인 <code>POST</code> /accounts/token/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| username | String | 아이디 |
| password | String | 비밀번호 |

- Response
    - `200 OK`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
    - `401 Unauthorized`
        - 정확한 정보를 입력하지 않은 경우

</details>

<details>
<summary> 가입 <code>POST</code> /accounts/signup/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| username | String | 아이디 |
| email | String | 이메일 |
| nickname | String | 닉네임 |
| birthdate | Date | 생년월일 |
| password | String | 비밀번호 |

- Response
    - `201 CREATED`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
        - 필드에 유효하지 않은 값을 입력한 경우
        - 아이디, 이메일, 닉네임이 중복된 경우

</details>

<details>
<summary> 비밀번호 변경 <code>PUT</code> /accounts/password/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| old | String | 기존 비밀번호 |
| pw | String | 새 비밀번호 |
| pw2 | String | 새 비밀번호 확인 |

- Response
    - `200 OK`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
        - 기존 비밀번호가 틀린 경우
        - 새 비밀번호와 새 비밀번호 확인이 일치하지 않는 경우

</details>

<details>
<summary> 계정 정보 변경 <code>PUT</code> /accounts/update/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| username | String | 아이디 |
| email | String | 이메일 |
| nickname | String | 닉네임 |
| birthdate | Date | 생년월일 |
| password | String | 비밀번호 |

- Response
    - `200 OK`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
        - 필드에 유효하지 않은 값을 입력한 경우
        - 아이디, 이메일, 닉네임이 중복된 경우

</details>

<details>
<summary> 계정 정보 일부 변경 <code>PATCH</code> /accounts/update/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| username | String | 아이디 |
| email | String | 이메일 |
| nickname | String | 닉네임 |
| birthdate | Date | 생년월일 |
| password | String | 비밀번호 |

- Response
    - `200 OK`
        - 빈 JSON이어도 `200`이 반환된다.
    - `400 Bad Request`
        - 필드에 유효하지 않은 값을 입력한 경우
        - 아이디, 이메일, 닉네임이 중복된 경우

</details>

<details>
<summary> 계정 삭제 <code>DELETE</code> /accounts/delete/ </summary>

- Response
    - `204 No Content`

</details>

### recipes

<details>
<summary> 레시피 리스트 <code>GET</code> /recipes/ </summary>

- Response
    - `200 OK`

</details>

<details>
<summary> 레시피 상세 <code>GET</code> /recipes/recipe_pk/ </summary>

- Response
    - `200 OK`
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우

</details>

<details>
<summary> 레시피 생성 <code>POST</code> /recipes/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| title | String | 제목 |
| content | String | 간단한 설명 |
| category | String | 분류 |
| time | Integer | 소요 시간 (단위: 분) |
| difficulty | Integer | 난이도 (최소 1, 최대 5) |
| ingredients | ManyToMany | 재료 |
| steps | ManyToMany | 조리 단계 |

`ingredients`는 `ingredient`와 `quantity`를 필드로 가진다.<br>
`steps`는 `detail`를 필드로 가진다.

- Example

```json
{
    "title": "Tomato Soup",
    "content": "Lava on Mustafar",
    "category": "Soup",
    "time": 60,
    "difficulty": 1,
    "ingredients": [
        {
            "ingredient": "tomato",
            "quantity": "four"
        },
        {
            "ingredient": "onion",
            "quantity": "one"
        },
        {
            "ingredient": "butter",
            "quantity": "20g"
        },
        {
            "ingredient": "chicken stock",
            "quantity": "0.5 cube"
        }
        {
            "ingredient": "garlic",
            "quantity": "10g"
        }
    ],
    "steps": [
        {
            "detail": "prepare ingredients"
        },
        {
            "detail": "you can use a frying pan or a pot"
        }
    ]
}
```

- Response
    - `201 CREATED`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우

</details>

<details>
<summary> 레시피 수정 <code>PUT</code> /recipes/recipe_pk/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| title | String | 제목 |
| content | String | 간단한 설명 |
| category | String | 분류 |
| time | Integer | 소요 시간 (단위: 분) |
| difficulty | Integer | 난이도 (최소 1, 최대 5) |
| ingredients | ManyToMany | 재료 |
| steps | ManyToMany | 조리 단계 |

`ingredients`는 `ingredient`와 `quantity`를 필드로 가진다.<br>
`steps`는 `detail`를 필드로 가진다.

- Response
    - `200 OK`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우

</details>

<details>
<summary> 레시피 부분 수정 <code>PATCH</code> /recipes/recipe_pk/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| title | String | 제목 |
| content | String | 간단한 설명 |
| category | String | 분류 |
| time | Integer | 소요 시간 (단위: 분) |
| difficulty | Integer | 난이도 (최소 1, 최대 5) |
| ingredients | ManyToMany | 재료 |
| steps | ManyToMany | 조리 단계 |

`ingredients`는 `ingredient`와 `quantity`를 필드로 가진다.<br>
`steps`는 `detail`를 필드로 가진다.

- Response
    - `200 OK`
    - `400 Bad Request`
        - 유효하지 않은 값을 입력한 경우
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우

</details>

<details>
<summary> 레시피 삭제 <code>DELETE</code> /recipes/recipe_pk/ </summary>

- Response
    - `204 No Content`
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우

</details>

<details>
<summary> 레시피 리뷰 작성 <code>PATCH</code> /recipes/recipe_pk/reviews/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| content | String | 내용 |

- Response
    - `201 OK`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우

</details>

<details>
<summary> 리뷰 리스트 <code>GET</code> /recipes/recipe_pk/reviews/ </summary>

- Response
    - `200 OK`
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우

</details>

<details>
<summary> 리뷰 상세 <code>GET</code> /recipes/recipe_pk/reviews/review_pk/ </summary>

- Response
    - `200 OK`
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우
        - 리뷰가 존재하지 않는 경우

</details>

<details>
<summary> 레시피 리뷰 수정 <code>PUT</code> /recipes/recipe_pk/reviews/review_pk/ </summary>

- Request parameters

| Parameter | Type | Description |
| --- | --- | --- |
| content | String | 내용 |

- Response
    - `201 OK`
    - `400 Bad Request`
        - 필드에 값을 입력하지 않은 경우
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우
        - 리뷰가 존재하지 않는 경우

</details>

<details>
<summary> 레시피 리뷰 삭제 <code>DELETE</code> /recipes/recipe_pk/reviews/review_pk/ </summary>

- Response
    - `204 No Content`
    - `404 Not Found`
        - 레시피가 존재하지 않는 경우
        - 리뷰가 존재하지 않는 경우

</details>