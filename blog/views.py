from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
all_posts = [
    {
        "slug":"Django-future-of-bankend",
        "image":"code1.jpg",
        "author": "Kennedy Akogo",
        "date": date(2022,12,21),
        "title":"How Django will be the most Prefered backend language",
        "excerpt":"You will not believe it",
        "content":  """
        Possimus at harum dignissimos dicta nesciunt
        exercitationem? Quisquam magni officiis eius distinctio quis quos repellendus hic, itaque laborum magni molestiae earum,
        dolorem ducimus consequuntur cupiditate dignissimos nulla sint, illum cupiditate sint maxime delectus veniam ullam quibusdam laudantium
        . Corrupti excepturi ea totam itaque beatae dicta inventore cupiditate quia officiis molestiae. Aperiam similique aspernatur vero, quaerat ipsum 
        corrupti veniam odit nostrum sed illo excepturi libero nihil. Provident maiores placeat aspernatur sunt delectus repellat perspiciatis accusantium numquam
        amet earum, maxime fugiat alias quas quo nulla, minus eligendi rem sit reiciendis modi eius ab deleniti magnam, similique velit facilis laudantium repellendus
        ipsum quidem sapiente. Hic ex enim provident itaque reiciendis dolore, aliquam animi 
        iste eaque magni enim cupiditate, recusandae 
        a aperiam corrupti sed
        
        Saepe qui reprehenderit excepturi earum omnis delectus tempore repellendus laudantium voluptatum laborum, 
        modi ipsam dolor blanditiis exercitationem tempore facere iste, veniam vitae architecto ea eaque nisi autem reprehenderit 
        voluptate sunt commodi, odit aliquid omnis inventore nisi exercitationem quas suscipit sequi. Fuga dolorum perspiciatis rerum. 
        Tempore similique alias maiores, voluptatibus magnam deserunt voluptatem totam non voluptas quo libero a.

        Nesciunt nisi corrupti quod fuga officia, modi quibusdam dicta, nesciunt saepe pariatur fuga culpa sapiente quos modi.
        Illum quam nulla placeat deserunt maiores ratione corrupti odio vero, eos amet laudantium fugiat inventore similique autem eum doloremque
        asperiores dolorum quasi, ipsa eos adipisci illo amet architecto, maxime consectetur ratione explicabo a vero perspiciatis eum tempore quisquam
        laboriosam ab, iste repellendus assumenda suscipit eaque? Dignissimos nemo sequi sit error, non aliquid et, doloremque reiciendis accusantium sequi,
        dignissimos dicta dolor blanditiis velit ullam illo delectus deleniti vitae dolores iste.

        Voluptatem reprehenderit vel adipisci, quod voluptatibus in debitis consequuntur deserunt quaerat blanditiis, 
        consectetur nisi doloremque nemo culpa eum eos error quisquam. Laborum officia optio eaque, suscipit beatae optio reiciendis similique 
        placeat animi assumenda quas itaque laboriosam iste. Perferendis beatae exercitationem soluta cumque eveniet natus quod accusantium, nesciunt 
        rerum tenetur sunt corrupti repellat, tenetur dicta quisquam eligendi ipsa eaque quam deserunt est expedita rem sequi?

        Illum dolor praesentium repellendus quae vel, facere commodi mollitia provident sint quasi recusandae doloribus magni 
        non nobi  s tempore, similique architecto quod ea ullam ipsa nesciunt tempora quaerat illo quas est, incidunt neque ipsam inventore 
        saepe vero adipisci nemo veritatis quaerat omnis, pariatur veniam animi ipsam veritatis placeat. Reiciendis dignissimos iure excepturi 
        quo facere voluptates laborum amet aliquid, eos mollitia necessitatibus veritatis natus tenetur vel.
        
        """
    },
    {
        "slug":"python-development",
        "image":"code.jpg",
        "author": "Kennedy Akogo",
        "date": date(2022,11,21),
        "title":"Why is Pyhton the most popular programming language",
        "excerpt":"This is a story of why python is so popular",
        "content":  """
        Possimus at harum dignissimos dicta nesciunt
        exercitationem? Quisquam magni officiis eius distinctio quis quos repellendus hic, itaque laborum magni molestiae earum,
        dolorem ducimus consequuntur cupiditate dignissimos nulla sint, illum cupiditate sint maxime delectus veniam ullam quibusdam laudantium
        . Corrupti excepturi ea totam itaque beatae dicta inventore cupiditate quia officiis molestiae. Aperiam similique aspernatur vero, quaerat ipsum 
        corrupti veniam odit nostrum sed illo excepturi libero nihil. Provident maiores placeat aspernatur sunt delectus repellat perspiciatis accusantium numquam
        amet earum, maxime fugiat alias quas quo nulla, minus eligendi rem sit reiciendis modi eius ab deleniti magnam, similique velit facilis laudantium repellendus
        ipsum quidem sapiente. Hic ex enim provident itaque reiciendis dolore, aliquam animi 
        iste eaque magni enim cupiditate, recusandae 
        a aperiam corrupti sed
        
        Saepe qui reprehenderit excepturi earum omnis delectus tempore repellendus laudantium voluptatum laborum, 
        modi ipsam dolor blanditiis exercitationem tempore facere iste, veniam vitae architecto ea eaque nisi autem reprehenderit 
        voluptate sunt commodi, odit aliquid omnis inventore nisi exercitationem quas suscipit sequi. Fuga dolorum perspiciatis rerum. 
        Tempore similique alias maiores, voluptatibus magnam deserunt voluptatem totam non voluptas quo libero a.

        Nesciunt nisi corrupti quod fuga officia, modi quibusdam dicta, nesciunt saepe pariatur fuga culpa sapiente quos modi.
        Illum quam nulla placeat deserunt maiores ratione corrupti odio vero, eos amet laudantium fugiat inventore similique autem eum doloremque
        asperiores dolorum quasi, ipsa eos adipisci illo amet architecto, maxime consectetur ratione explicabo a vero perspiciatis eum tempore quisquam
        laboriosam ab, iste repellendus assumenda suscipit eaque? Dignissimos nemo sequi sit error, non aliquid et, doloremque reiciendis accusantium sequi,
        dignissimos dicta dolor blanditiis velit ullam illo delectus deleniti vitae dolores iste.

        Voluptatem reprehenderit vel adipisci, quod voluptatibus in debitis consequuntur deserunt quaerat blanditiis, 
        consectetur nisi doloremque nemo culpa eum eos error quisquam. Laborum officia optio eaque, suscipit beatae optio reiciendis similique 
        placeat animi assumenda quas itaque laboriosam iste. Perferendis beatae exercitationem soluta cumque eveniet natus quod accusantium, nesciunt 
        rerum tenetur sunt corrupti repellat, tenetur dicta quisquam eligendi ipsa eaque quam deserunt est expedita rem sequi?

        Illum dolor praesentium repellendus quae vel, facere commodi mollitia provident sint quasi recusandae doloribus magni 
        non nobi  s tempore, similique architecto quod ea ullam ipsa nesciunt tempora quaerat illo quas est, incidunt neque ipsam inventore 
        saepe vero adipisci nemo veritatis quaerat omnis, pariatur veniam animi ipsam veritatis placeat. Reiciendis dignissimos iure excepturi 
        quo facere voluptates laborum amet aliquid, eos mollitia necessitatibus veritatis natus tenetur vel.
        
        """
    },
    {
        "slug":"Programing-is-Great",
        "image":"code2.jpg",
        "author": "Kennedy Akogo",
        "date": date(2022,10,21),
        "title":"The Joy of Prograiming",
        "excerpt":"I believe Everyon should learn to code",
        "content":  """
        Possimus at harum dignissimos dicta nesciunt
        exercitationem? Quisquam magni officiis eius distinctio quis quos repellendus hic, itaque laborum magni molestiae earum,
        dolorem ducimus consequuntur cupiditate dignissimos nulla sint, illum cupiditate sint maxime delectus veniam ullam quibusdam laudantium
        . Corrupti excepturi ea totam itaque beatae dicta inventore cupiditate quia officiis molestiae. Aperiam similique aspernatur vero, quaerat ipsum 
        corrupti veniam odit nostrum sed illo excepturi libero nihil. Provident maiores placeat aspernatur sunt delectus repellat perspiciatis accusantium numquam
        amet earum, maxime fugiat alias quas quo nulla, minus eligendi rem sit reiciendis modi eius ab deleniti magnam, similique velit facilis laudantium repellendus
        ipsum quidem sapiente. Hic ex enim provident itaque reiciendis dolore, aliquam animi 
        iste eaque magni enim cupiditate, recusandae 
        a aperiam corrupti sed
        
        Saepe qui reprehenderit excepturi earum omnis delectus tempore repellendus laudantium voluptatum laborum, 
        modi ipsam dolor blanditiis exercitationem tempore facere iste, veniam vitae architecto ea eaque nisi autem reprehenderit 
        voluptate sunt commodi, odit aliquid omnis inventore nisi exercitationem quas suscipit sequi. Fuga dolorum perspiciatis rerum. 
        Tempore similique alias maiores, voluptatibus magnam deserunt voluptatem totam non voluptas quo libero a.

        Nesciunt nisi corrupti quod fuga officia, modi quibusdam dicta, nesciunt saepe pariatur fuga culpa sapiente quos modi.
        Illum quam nulla placeat deserunt maiores ratione corrupti odio vero, eos amet laudantium fugiat inventore similique autem eum doloremque
        asperiores dolorum quasi, ipsa eos adipisci illo amet architecto, maxime consectetur ratione explicabo a vero perspiciatis eum tempore quisquam
        laboriosam ab, iste repellendus assumenda suscipit eaque? Dignissimos nemo sequi sit error, non aliquid et, doloremque reiciendis accusantium sequi,
        dignissimos dicta dolor blanditiis velit ullam illo delectus deleniti vitae dolores iste.

        Voluptatem reprehenderit vel adipisci, quod voluptatibus in debitis consequuntur deserunt quaerat blanditiis, 
        consectetur nisi doloremque nemo culpa eum eos error quisquam. Laborum officia optio eaque, suscipit beatae optio reiciendis similique 
        placeat animi assumenda quas itaque laboriosam iste. Perferendis beatae exercitationem soluta cumque eveniet natus quod accusantium, nesciunt 
        rerum tenetur sunt corrupti repellat, tenetur dicta quisquam eligendi ipsa eaque quam deserunt est expedita rem sequi?

        Illum dolor praesentium repellendus quae vel, facere commodi mollitia provident sint quasi recusandae doloribus magni 
        non nobi  s tempore, similique architecto quod ea ullam ipsa nesciunt tempora quaerat illo quas est, incidunt neque ipsam inventore 
        saepe vero adipisci nemo veritatis quaerat omnis, pariatur veniam animi ipsam veritatis placeat. Reiciendis dignissimos iure excepturi 
        quo facere voluptates laborum amet aliquid, eos mollitia necessitatibus veritatis natus tenetur vel.
        
        """
    },


]
def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    lastest_post = sorted_posts[-3:]   
    
    return render(request, "blog/index.html",{
        "posts":lastest_post
    })
    #return HttpResponse("<h1>This is the starting page</h1>")

def all_post(request):
    #return HttpResponse("<h1>This is the starting page</h1>1111")
    return render(request,"blog/all_post.html",{
        "all_posts":all_posts
    })

def single_post_page(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html ",{
        "post":identified_post
    })