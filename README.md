source myvenv/bin/activate    
python3 -m pip install --upgrade pip   
echo 'Django~=3.2.10' > requirements.txt
pip install -r requirements.txt  
django-admin startproject mc .    
vi mc/settings.py    
python3 manage.py migrate      
➜  ~ https://stackoverflow.com/questions/23048129/python-name-os-is-not-defined
python manage.py runserver   ➜                                              
➜  ~ python manage.py createsuperuser 
➜  ~ python manage.py startapp shop     
➜  ~ python manage.py migrate shop                                                                   
➜  ~ python manage.py makemigrations shop                             
~ vi shop/urls.py                                
➜  ~ vi shop/views.py                      
vi templates/post_list.html  