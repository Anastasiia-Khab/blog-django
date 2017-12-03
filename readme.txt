#cd djangogirls
#myvenv\Scripts\activate
#git init
#####git config --global user.name Anastasiia-Khab
#####git config --global user.email you@example.com
#git status
#git add --all .
#git commit -m "My Django Girls app, ..... commit"
#git remote add origin https://github.com/Anastasiia-Khab/blog-django.git
#git push -u origin master
#or####git push

#Open up the PythonAnywhere consoles page and go to your Bash console (or start a new one).
#cd ~/blog-django
#git pull

#cd djangogirls
#myvenv\Scripts\activate
#python manage.py runserver

#python manage.py shell
#from blog.models import Post
#from django.contrib.auth.models import User
#Post.objects.all()
#me = User.objects.get(username='anastasy')
#Post.objects.filter(author=me)
#Post.objects.create(author=me, title='Sample title', text='Test')
#Post.objects.filter(title__contains='title')
#from django.utils import timezone
#Post.objects.filter(published_date__lte=timezone.now())
#Post.objects.order_by('created_date')
#Post.objects.order_by('-created_date')
#Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
#exit()
