# A. Base.html
```{% load static %}
    <img src="{% static 'movies/header.jpg' %}" alt="header"/>
    {% block content %}
    {% endblock content %}
```
body 부분에 위 코드를 넣어줘서 img를 static으로부터 꺼내 쓸 수 있게 구성해주었고, block을 통해 다른 html 데이터들을 상속하여 쓸 수 있게 만들어주었다.
기존 CRUD 연습했던 것 그대로 작성해서 쉽게 해결 할 수 있었다.

# B. index.html
index 부분에 주석으로 처리한 부분을 살리면 요구 사항에 맞게 사용할 수 있다. 해당 영화의 제목과, 평점을 표시하고 영화 제목 클릭시 해당 상세 조회 페이지로 이동 할 수 있도록 구성해주었다. 이것도 기존 CRUD 연습했던 것 그대로 작성해서 쉽게 해결 할 수 있었다.

# C. detail.html
영화 상세보기 페이지를 구현해주었고, 일부 버튼을 부트스트랩을 이용해서 간단하게 꾸며주었다. 요구조건에 맞추어 작성하였따.

# D. create.html
영화를 생성하기 위한 from 요소들을 표현하게 구성해주었다. 다만 여기서 추가 요구사항인 form에서 날짜를 받는 형태와, 숫자 범위 지정 및 장르 고를 수 있게 만들어 주었다. form을 변경해주는 과정은 구글링을 통해서 찾아내서 작성할 수 있었고, 이미지는 media를 이용해서 등록할 수 있도록 작성해 주었다.

# E. update.html
영화 내용을 수정할 수 있도록 버튼을 만들어서 수정할 수 있게 만들어주었다. 여기서 수정하다가 다시 수정 전으로 이동하기 위한 reset 버튼을 만들어 주었다.

# F. 선택과제
TMDB의 API를 따오는 것 까지는 성공했다. 다만, 이것을 데이터베이스에 반영해서 출력하는 형식까지 구현하는 것엔 어려움이 있어 성공하지 못했고, Api를 이용해 index에 영화들의 포스터만 가져오는 형태를 만들어 낼 수 있었다.
API를 database에 입력하는 방법을 찾지 못해서 이 부분에서 어려움을 많이 느꼈다. 다만, 이전 pjt에서 활용했던 것을 활용해 api를 따오는 시도에 성공한 점은 좋았던거 같다.
추가적으로 부트스트랩을 이용해서 몇몇 a태그를 사용한 링크들을 버튼형식으로 간단하게 꾸며주었다.

# 전체 느낀점
A~E는 수업시간에 반복해서 한 내용들을 통해서 작성하는 것들이었으므로 크게 어려움이 없었다. 다만 선택 과제를 시도해보면서 API를 따와서 데이터베이스에 넣어 출력해 표로 표시해보고 싶었으나, 성공하지 못한 점에서 조금 아쉬움이 많이 남았다. 