# drf
1번은 코드로 남겨놨습니다.


문제2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
mutable 주소값

immutable 값을 저장

deepcopy(mutable) 주소값으로 들어가지않고 값으로 들어간다  list_ = mutable[:] == 요것또한비슷한맥락

# x와 z가 같은 객체를 공유하지 않는다.(리스트만 가능)
z = x[:]

# deepcopy를 이용하면 x와 cpy가 같은 객체를 공유하지 않는다.
dcpy = copy.deepcopy(x)

출처: https://ledgku.tistory.com/54 [블로그:티스토리]

string = immutable
list_ = mutable
string += " immmutable string!!"
list_.append = "mutable string!!"

문제(검색)2. mutable, immutable 특성
[특성]
mutable : 변할 수 있는 값
immutable : 변할 수 없는 값

[해당되는 자료형]
mutable : list, dictionary, set 등
immutable : int, float, string, tuple 등


문제 3. DB Field의 Key 종류와 특징
[Key]
릴레이션(=테이블)
- 데이터베이스의 데이터들을 표의 형태로 표현한 것

튜플 : Tuple
- 릴레이션을 구성하는 행
- 튜플의 수를 기수(Cardinality)라고 부른다.

속성 : Attribute
- 릴레이션을 구성하는 열
- 속성의 수를 차수(Degree)라고 부른다.

[키 종류와 특징]
후보키 : Candidate Key
- 릴레이션을 구성하는 속성들 중 튜플을 유일하게 식별할 수 있는 속성들의 부분 집합
- 모든 릴레이션은 하나 이상의 후보키를 가져야하며 유일성(Unique)과 최소성(Minimality)을 만족해야 한다.

기본키 : Primary Key
- 후보키 중에서 선택한 주가 되는 키
- 릴레이션에서 특정 레코드를 유일하게 식별할 수 있는 속성, Null 값으로 둘 수 없다.

대체키 : Replacement Key
- 후보키 중에서 기본키를 제외한 나머지 속성들

외래키 : Foreign Key
- 관계를 맺는 릴레이션 간에 기본키를 참조하는 속성
- 하나의 릴레이션에는 다수의 외래키가 존재할 수 있다.
- 외래키로 지정된 필드는 중복 및 Null 값으로 둘 수 있다.

슈퍼키 : Super Key
- 하나의 릴레이션 내에 있는 속성들의 집합
- 슈퍼키로 구성된 속성의 집합은 동일한 값으로 나타나지 않는다.
- 릴레이션을 구성하는 튜플들에 대해 유일성은 만족하나 최소성은 만족하지 못한다.


문제 4. django의 object, queryset
object : DB 모델에 대한 객체
queryset : DB 모델에서 전달받은 객체(object)들의 목록

[ORM 활용 명령어 사용 방법]
[Model명].objects.~

[불러오기]
.all() : 전체 데이터 불러오기
.get() : 하나의 데이터 불러오기

[조회]
.filter() : 조건에 해당되는 데이터 조회
.exclude() : 조건에 해당되지 않는 데이터 조회

[생성]
.create() : 해당되는 모델 객체에서 원하는 데이터를 생성

[삭제]
.delete() : 해당되는 모델 객체에서 원하는 데이터를 삭제

[정렬]
.order_by() : 오름차순 '필드명' / 내림차순 '-필드명'
