# .get() 메서드를 활용해 dictionary를 조금 더 깔끔하게 생성할 수 있음

# 다음 두 코드는 같은 기능을 수행하는 다른 함수를 잘라온 것인데 위는 아래보다 변수가 두배가 들어가기에 성능적으로 예쁘지 못하다.
# 그냥 한 눈에 보기에도 차이가 난다는 게 보인다.
# 함수의 key 값을 재정의 할 때 사용한다.
# 상황에 따라 둘 중 하나를 선택해서 사용하면 좋을 듯 하다.

data_list = []
for i in range(len(movies)):
    data_dict = {} 
    data_dict['id'] = movies[i]['id']
    data_dict['title'] = movies[i]['title']
    data_dict['revenue'] = movies[i]['revenue']
    data_dict['overview'] = movies[i]['overview']
    data_dict['genre_ids'] = movies[i]['genre_ids']
    data_dict['poster_path'] = movies[i]['poster_path']

    for i in range(len(data_dict['genre_ids'])):
        for id in genres:
            if data_dict['genre_ids'][i] == id['id']:
                data_dict['genre_ids'][i] = id['name']

    data_list.append(data_dict)

#---------------------#

artist_data_list = []   
for artist in artists:
    artist_data_dict = {
        'id' : artist.get('id'),
        'name' : artist.get('name'),
        'images' : artist.get('images'),
        'type' : artist.get('type')
    }
    
    genres_name_list = []
    for id in range(len(genres)):
        for i in artist['genres_ids']:
            if genres[id]['id'] == i:
                genres_name_list.append(genres[id]['name'])
        artist_data_dict['genres_names'] = genres_name_list
            
    artist_data_list.append(artist_data_dict)


#---------------------------------------#

# 3. 출판일을 기준으로 최신 도서 10개 추출 (hint: sorted 함수 key 속성)
latest_books = sorted(
    books, key = lambda x: datetime.strptime(x['pubDate'], '%Y-%m-%d'), reverse=True
    )[:10]

# 출판일을 기준으로 최신 도서 10개 추출
data_dict = {}
for i in parsed_data:
    data_dict[i["title"]] = i["pubDate"]
sorted_dict = sorted(data_dict.items(), key = lambda x: x[1])
new_arrival = []  # 최신 도서 10개를 추출
for i in range(10):
    new_arrival.append(sorted_dict.pop(-1))

# 놀랍게도 위와 아래가 완벽하게 똑같은 기능을 하는 코드
# 위의 코드가 훨씬 가독성도 좋고 간단합니다.
# lambda와 datetime의 개념을 정립해야겠다고 생각했고 리버스나 슬라이싱 기능 또한 적극 활용해 습관을 들여야겠습니다.
# 한 줄의 코드로 많이 배웠습니다.

#-------------------------------------------#

# collections 모듈의 defaultdict에 대해서도 알게되었는데 알고리즘 문제를 풀며 존재한다는 건 알고 있었지만
# 사용하면 어떤 점이 편리하고 어떤 기능을 하는지 정확하게 알지 못했고 알려하지 않았습니다.
# 하지만 위의 lambda나 datetime의 경우와 비슷하게 코드의 양을 매우 크게 줄일 수 있는 수단이라는걸 오늘 알아버려서
# 빠른 시일 내에 학습할 예정입니다.

#----------------------------------------#

# 오늘 수업에서 문자열과 리스트의 메서드를 배웠습니다. 원래 사용하고 있던 기능도 있지만 잘 모르고 알더라도 잘 쓰지 않던 메서드들의 필요성을 알아
# 철저히 복습해 사고의 과정에 넣을 수 있도록 하고 싶습니다.