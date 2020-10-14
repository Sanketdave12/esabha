from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from social.models import FollowUser, MyPost, MyProfile, PostComment, PostLike
from social.myserializer import PostLikeSerializer,MyProfileSerializer , PostCommentSerializer , FollowUserSerializer ,MyPostSerializer , UserSerializer
from django.views.generic.detail import DetailView
from django.db.models import Q
from django.views.generic.edit import UpdateView, CreateView ,DeleteView
from django.http.response import HttpResponseRedirect
from rest_framework import viewsets 
from django.contrib.auth.models import User

# Create your views here.
@method_decorator(login_required, name="dispatch")    
class HomeView(TemplateView):
    template_name = "social/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        followedlist = FollowUser.objects.filter(followed_by=self.request.user.myprofile)
        followedlist2 = []
        for i in followedlist:
            followedlist2.append(i.profile)
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        postlist = MyPost.objects.filter(Q(uploaded_by__in = followedlist2) | Q(uploaded_by__isnull=True)).filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by("-id")
        for i in postlist:
            i.liked = False
            ob = PostLike.objects.filter(post = i, liked_by = self.request.user.myprofile)
            if ob:
                i.liked = True
            ob = PostLike.objects.filter(post = i)
            i.likecount = ob.count()
        context["mypost_list"] = postlist 
        return context
    



class AboutView(TemplateView):
    template_name = "social/about.html"

class ContactView(TemplateView):
    template_name = "social/contact.html"

def follow(req,pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.create(profile=user, followed_by = req.user.myprofile)
    return HttpResponseRedirect(redirect_to ="/social/myprofile")

def unfollow(req,pk):
    user = MyProfile.objects.get(pk=pk)
    FollowUser.objects.filter(profile=user, followed_by = req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to ="/social/myprofile")

def like(req,pk):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.create(post=post, liked_by=req.user.myprofile)
    return HttpResponseRedirect(redirect_to= "/social/home")

def unlike(req,pk):
    post = MyPost.objects.get(pk=pk)
    PostLike.objects.filter(post=post, liked_by=req.user.myprofile).delete()
    return HttpResponseRedirect(redirect_to= "/social/home")





@method_decorator(login_required, name="dispatch")    
class MyProfileUpdateView(UpdateView):
      model = MyProfile
      fields = ["name","age","address","status","gender","phone_no","description","pic"]

@method_decorator(login_required, name="dispatch")    
class MyPostCreate(CreateView):
     model = MyPost
     fields = ["pic","subject", "msg"]
     def form_valid(self, form):
         self.object = form.save()
         self.object.uploaded_by = self.request.user.myprofile
         self.object.save()
         return HttpResponseRedirect(self.get_success_url())

@method_decorator(login_required, name="dispatch")    
class MyPostListView(ListView):
    model = MyPost
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MyPost.objects.filter(Q(uploaded_by = self.request.user.myprofile) | Q(uploaded_by__isnull=True)).filter(Q(subject__icontains = si) | Q(msg__icontains = si)).order_by("-id")
 


@method_decorator(login_required, name="dispatch")    
class MyPostDetailView(DetailView):
    model = MyPost
 
@method_decorator(login_required, name="dispatch")    
class MyPostDeleteView(DeleteView):
    model = MyPost

@method_decorator(login_required, name="dispatch")    
class MyProfileListView(ListView):
    model = MyProfile
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        proflist = MyProfile.objects.filter(Q(name__icontains = si) | Q(address__icontains = si) | Q(gender__icontains = si) | Q(status__icontains = si)).order_by("-id")
        for i in proflist:
            i.followed = False
            ob = FollowUser.objects.filter(profile = i, followed_by = self.request.user.myprofile)
            if ob:
                i.followed = True
        return proflist

@method_decorator(login_required, name="dispatch")    
class MyProfileDetailView(DetailView):
    model = MyProfile


class PostLikeViewSet(viewsets.ModelViewSet):
    queryset = PostLike.objects.all().order_by('-id') 
    serializer_class = PostLikeSerializer

class MyPostViewSet(viewsets.ModelViewSet):
    queryset = MyPost.objects.all().order_by('-id') 
    serializer_class = MyPostSerializer
    

class PostCommentViewSet(viewsets.ModelViewSet):
    queryset = PostComment.objects.all().order_by('-id') 
    serializer_class = PostCommentSerializer

class FollowUserViewSet(viewsets.ModelViewSet):
    queryset = FollowUser.objects.all().order_by('-id') 
    serializer_class = FollowUserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id') 
    serializer_class = UserSerializer

class MyProfileViewSet(viewsets.ModelViewSet):
    queryset = MyProfile.objects.all().order_by('-id') 
    serializer_class = MyProfileSerializer