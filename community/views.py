from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from crawling.models import BlogData
from django.utils import timezone
from .forms import  *
from django.views.generic.edit import FormView
from django.db.models import Q

from django.core.paginator import Paginator
# Create your views here.
def index(request):
    post_list = Blog.objects.all().order_by('-id')
    news_list=BlogData.objects.all().order_by('-id')
    comment_list = Comment.objects.all().order_by('-id')
    paginatorPost = Paginator(post_list,5)
    paginatorNews = Paginator(news_list,5)
    paginatorComment = Paginator( comment_list,5)
    page = request.GET.get('page')
    Posts = paginatorPost.get_page(page)
    News = paginatorNews.get_page(page)
    Comments = paginatorComment.get_page(page)
    return render(request,"index.html",{'postList':Posts,'newsList':News,'commentList':Comments})
def allPost(request):
    posts=Blog.objects.all().order_by('-id')
    return render(request,"allPost.html",{'blogContents':posts})
#게시판 카테고리 10개
def pre10(request):
    posts=Blog.objects.filter( category = ['0']).order_by('-id')
    age=0
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def y10(request):
    posts=Blog.objects.filter( category = ['1']).order_by('-id')
    age=1
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def y20(request):
    posts=Blog.objects.filter( category = ['2']).order_by('-id')
    age=2
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def y30_40(request):
    posts=Blog.objects.filter( category = ['3']).order_by('-id')
    age=3
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def y50_60(request):
    posts=Blog.objects.filter( category = ['4']).order_by('-id')
    age=4
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def over70(request):
    posts=Blog.objects.filter( category = ['5']).order_by('-id')
    age=5
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def moderna(request):
    posts=Blog.objects.filter( category = ['6']).order_by('-id')
    age=6
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def pfizer(request):#화이자백신 카테고리
    posts=Blog.objects.filter( category = ['7']).order_by('-id')
    age=7
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def az(request):
    posts=Blog.objects.filter( category = ['8']).order_by('-id')
    age=8
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def janssen(request): #얀센 백신 카테고리
    posts=Blog.objects.filter( category = ['9']).order_by('-id')
    age=9
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
def free(request): #자유게시판
    posts=Blog.objects.filter( category = ['10']).order_by('-id')
    age=10
    return render(request,"allPost.html",{'blogContents':posts,'age':age})
#상세창
def detail(request,postId):
    post = get_object_or_404(Blog,pk=postId) 
    comments = Comment.objects.filter(postId=postId,comment_id__isnull=True)
    re_comments=[]
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    commentForm = CommentForm()
    return  render(request,'detail.html',{'postContents':post,'comments':comments,'re_comments':re_comments,'commentForms':commentForm})

#새로운 글 작성
def new(request):
    if request.method == 'POST': #글 작성 후 저장버튼 눌렀을 때
        post_form = BlogForm(request.POST,request.FILES)
        context = {}
        categoryform=  CategoryForm(request.POST )
        print(categoryform)
        context['categoryform'] = categoryform
        if post_form.is_valid():# 이 form을 유효한지 검사후 유효하면 save해줌 (임시저장)
            post = post_form.save(commit = False)#임시저장 해주는 이유는 model에 있는 필드 중 new date를 안 담았음 (commit=False)
            post.category = categoryform.cleaned_data.get("category_field")
            #print(post.category)
            post.CustomUser = request.user
            post.writer = request.user
            post.pub_date = timezone.now() 
            post.save()
            return redirect("detailPage",post.id)
    else:
        post_form = BlogForm()
        context = {}
        context['categoryform'] = CategoryForm()
        context['postsform'] = post_form
        return render(request,'new.html',context)
    #댓글작성
def create_comment(request, postId):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            #이부분왜 id할당이 아니라 제목이 할당되지
            comment.postId = Blog.objects.get(pk = postId)
            #
            comment.post_id = postId
            #
            comment.CustomUser = request.user
            comment.writer = request.user
            comment.pub_date = timezone.now()
            comment.save()
    return redirect('/community/detailPage/'+str(postId))
#대댓글작성
def create_re_comment(request, postId, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.postId = Blog.objects.get(pk = postId)
            comment.post_id = postId
            comment.writer = request.user
            comment.CustomUser = request.user
            comment.comment_id = Comment.objects.get(pk = comment_id)
            comment.pub_date = timezone.now()
            comment.save()
    return redirect('/community/detailPage/'+str(postId))

#수정
def edit(request,postId):
    post = get_object_or_404(Blog,pk=postId)
    context = {}
    categoryform=  CategoryForm(request.POST )
    print(categoryform)
    context['categoryform'] = categoryform
    if request.method == 'GET': #수정
        post_form=BlogForm(instance=post)
        context = {}
        context['categoryform'] = CategoryForm()
        context['edit_post'] = post_form
        return render(request,'edit.html',context)
    else:
        post_form = BlogForm(request.POST,request.FILES,instance = post)
        if post_form.is_valid():
            post = post_form.save(commit = False)
            post.category = categoryform.cleaned_data.get("category_field")
            post.new_date = timezone.now() # 날짜 생성
            post.save()
        return redirect("detailPage",post.id)
# 댓글 수정
def update_review(request, post_id, comment_id):
    com=Comment.objects.get(id= comment_id)
    com_form=CommentForm(instance=com)
    if request.method == "POST":
        update_form= CommentForm(request.POST, instance = com)
        if update_form.is_valid():
            update_form.save()
            return redirect('/community/detailPage/'+ str(post_id))
    return render(request, 'review_update.html',{'com_form':com_form})

#게시글 삭제
def delete(request,postId):
   deletePost = get_object_or_404(Blog,pk=postId)
   deletePost.delete() #삭제해주는 메소드
   return redirect('allPost')
   #댓글삭제
def deleteComment(request,postId,commentId):
   deleteComment = get_object_or_404(Comment,pk=commentId)
   deleteComment.delete() #삭제해주는 메소드
   return redirect("detailPage",postId)
'''
def deleteAll(request):#관리자일 경우만 전체 게시물 삭제가능하도록 하기
    deleteAll = Blog.objects.all()
    deleteAll.delete()
    return redirect('allPost')'''
#검색
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Blog.objects.filter(Q(title__icontains=searchWord) | Q(body__icontains=searchWord) ).distinct().order_by('-id')

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

