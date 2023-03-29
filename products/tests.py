from django.test import TestCase
from .models import Mobile, Book
from django.urls import reverse


class TestProducts(TestCase):
    def setUp(self):
        self.mobile = Mobile.objects.create(
            name='name',
            description='description',
            price='1',
            old_price='2',
            category='category',
            image='image',
            weight='1',
            colors='colors',
        )

        self.book = Book.objects.create(
            title='title1',
            author='author1',
            text='text1',
            image='image1',
            price='5'
        )

    def test_mobile_list_url(self):
        response = self.client.get('/')
        return self.assertEqual(response.status_code, 200)

    def test_mobile_list_name(self):
        response = self.client.get(reverse('products:mobile_list'))
        return self.assertEqual(response.status_code, 200)

    def test_mobile_list_template(self):
        response = self.client.get(reverse('products:mobile_list'))
        return self.assertTemplateUsed(response, 'products/mobile_list.html')

    def test_mobile_list_contains(self):
        response = self.client.get(reverse('products:mobile_list'))
        return self.assertContains(response, self.mobile)

    def test_mobile_detail_url(self):
        response = self.client.get(f'/detail_mobile/{self.mobile.id}')
        return self.assertEqual(response.status_code, 301)

    def test_mobile_detail_name(self):
        response = self.client.get(reverse('products:mobile_detail', args=[self.mobile.id]))
        return self.assertTrue(response.status_code, 301)

    def test_mobile_detail_template(self):
        response = self.client.get(reverse('products:mobile_detail', args=[self.mobile.id]))
        return self.assertTemplateUsed(response, 'products/mobile_detail.html')

    def test_mobile_detail_contain(self):
        response = self.client.get(reverse('products:mobile_detail', args=[self.mobile.id]))
        return self.assertContains(response, self.mobile)

    def test_comment_mobile_url(self):
        response = self.client.get(f'/comment_mobile/{self.mobile.id}')
        return self.assertEqual(response.status_code, 301)

    def test_book_list_url(self):
        response = self.client.get('/book/')
        return self.assertEqual(response.status_code, 200)

    def test_book_list_name(self):
        response = self.client.get(reverse('products:book_list'))
        return self.assertEqual(response.status_code, 200)

    def test_book_list_template(self):
        response = self.client.get(reverse('products:book_list'))
        return self.assertTemplateUsed(response, 'products/book_list.html')

    def test_book_list_contain(self):
        response = self.client.get(reverse('products:book_list'))
        self.assertContains(response, self.book.price)
        self.assertContains(response, self.book.image)
        return self.assertContains(response, self.book.title)

    def test_book_detail_url(self):
        response = self.client.get(f'/book_detail/{self.book.id}')
        return self.assertEqual(response.status_code, 301)

    def test_book_detail_name(self):
        response = self.client.get(reverse('products:book_detail', args=[self.book.id]))
        return self.assertEqual(response.status_code, 200)

    def test_book_detail_template(self):
        response = self.client.get(reverse('products:book_detail', args=[self.book.id]))
        return self.assertTemplateUsed(response, 'products/book_detail.html')

    def test_book_detail_contain(self):
        response = self.client.get(reverse('products:book_detail', args=[self.book.id]))
        return self.assertContains(response, self.book.title)

    def test_comment_book_url(self):
        response = self.client.get(f'/comment_book/{self.book.id}')
        return self.assertEqual(response.status_code, 301)

