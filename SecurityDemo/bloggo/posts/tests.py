# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .views import about, post_details
from .models import Post

# Create your tests here.
class AboutPage(TestCase):
    def setUp(self):
        self.c = Client()
        self.r = self.c.get("/posts/about")
    def testUrlResponse(self):
        response = self.r
        self.assertTrue(response.status_code == 200 or response.status_code == 301,
                         "The About HTTP response should return an OK status code and not a 404")
        self.assertEqual(response.resolver_match.func, about,
                         "The URL /posts/about should resolve to the 'about' view function")
        self.assertEqual(len(response.templates), 2,
                         "The about page template should extend the base.html template")
        self.assertEqual(response.templates[1].name, "posts/base.html",
                         "The about page template should extend the base.html template")
        self.assertEqual(response.templates[0].name, "posts/about.html",
                         "The about page template should extend the base.html template")
        self.assertTrue(b"Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars"
                        in response.content,
                         "The about page should contain the string "
                         "'Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars'")

class PostDetailsPage(TestCase):
    def setUp(self):
        Post.objects.create(title="Worst Day Ever",
                            body="So I was walking outside today and some guy comes up to with a clipboard wearing a "
                                 "freshly ironed pair of salmon colored chinos and he's like Hey do you care about the "
                                 "environment. And I'm like yo of course I care about the environment who do you think I "
                                 "am some kind of self serving schmuck of course I care about the world I live in and how "
                                 "we as humans affect it and stuff. So yeah. Then hes like well thats great news Im part "
                                 "of an organization called CalPIRG and you should totally join it if you dont youre an "
                                 "earth hating piece of crap except he didnt actually say that but you could totally see "
                                 "that was like the vibe he was giving off. So then Im like ok Ill join your stupid "
                                 "organization and filled out his form n stuff n then hes like well sykes buddy now "
                                 "youre gonna pay $10 a semester to my club and im gonna spend it on big bouncy "
                                 "castles and liquor for all my friends and I was like oh my god you conniving insidious "
                                 "nefarious poopheads gimme back my money but then he was like too late you already signed "
                                 "the form and thats the worst day of my life!")
        Post.objects.create(title="Important Questions",
                            body="What job did Chandler Bing from friends have?")
        self.c = Client()
        self.r = self.c.get("/posts/details/1")
        self.r2 = self.c.get("/posts/details/2")
    def testUrlResponse(self):
        self.assertTrue(self.r.status_code == 200 or self.r.status_code == 301,
                         "The Post Details HTTP response should return an OK status code and not a 404")
        self.assertTrue(self.r2.status_code == 200 or self.r2.status_code == 301,
                         "The Post Details HTTP response should return an OK status code and not a 404")
        self.assertEqual(self.r.resolver_match.func, post_details,
                         "The URL /posts/details/<pk> should resolve to the 'post_details' view function "
                         "with argument pk=<pk>")
        self.assertEqual(self.r2.resolver_match.func, post_details,
                         "The URL /posts/details/<pk> should resolve to the 'post_details' view function "
                         "with argument pk=<pk>")
    def testResponseContent(self):
        self.assertEqual(len(self.r.templates), 2,
                         "The post details template should extend the base.html template")
        self.assertEqual(self.r.templates[1].name, "posts/base.html",
                         "The post details template should extend the base.html template")
        self.assertTrue(b"Worst Day Ever" in self.r.content,
                        "The URL /posts/details/1 should contain the content of the post with pk=1 (Worst Day Ever)")
        self.assertFalse(b"Chandler" in self.r.content,
                         "The URL /posts/details/1 should not contain the content of any other posts")
        self.assertTrue(b"Chandler" in self.r2.content,
                        "The URL /posts/details/2 should contain the content of the post with pk=2 (Important Questions)")
        self.assertFalse(b"Worst Day Ever" in self.r2.content,
                         "The URL /posts/details/2 should not contain the content of any other posts")