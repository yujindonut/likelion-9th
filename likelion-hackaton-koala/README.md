# ll20210731


git clone https://github.com/moongpom/Koala_a_som.git

git clone 한 뒤에 순서대로 입력하기

git init

python -m venv myvenv

source myvenv/Scripts/activate

cd Koala_a_som 

pip install django

pip install django-allauth

pip install pillow

pip install bs4

pip install requests

pip install django-crispy-forms

python manage.py makemigrations

python manage.py migrate

#(superuser 이 계정으로 로그인해도 되고 새로만들어도 됨

#id : pom 
#pw : aa112233)

#뉴스 기사 크롤링한거 업데이트하는 python parser.py 이건 나중에 데이터 업데이트 할 때 

python manage.py runserver

