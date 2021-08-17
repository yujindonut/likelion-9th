# teamproject_webtoon

git clone https://github.com/yujindonut/teamproject_webtoon.git

git init

python -m venv myvenv

source myvenv/Scripts/activate

cd webtoon

pip install django

python -m pip install --upgrade pip (업그레이드 안되어있다고 떠있을 시!!)

python manage.py collectstatic

pip install django-crispy-forms

pip install pillow

pip install django-imagekit

python manage.py makemigrations 

python manage.py migrate

python manage.py runserver

@superuser 계정

id : webtoon pw : aa1122
