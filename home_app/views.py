from django.shortcuts import render

# Create your views here.
def homeView(request):

    context = {
        'username' : 'Sadaf',
		'email' : 'sadaf@gmail.com',
        'text' : 'Greetings,Hope you are doing well. I represent Tech Mahindra, we are looking for SDET Architect Java automation Test Architect with Selenium for a long term Contract in St. Loius, MO.',
    }
    return render(request, 'home.html', context)


def aboutView(request):

    context = {
        'username' : 'Aisha',
		'email' : 'aisha@gmail.com',
        'text' : 'Greetings Aisha,Hope you are doing well. We are looking for SDET Architect Java automation Test Architect with Selenium for a long term Contract in St. Loius, MO.',
        'text1' : 'We only eat bananas on Saturdays.',
        'text2' : 'We love making playing football on rainy days.',
    }
    return render(request, 'about.html', context)



def getView(request, **kwargs):
    
    context = {
    
        'data':[
            {
                'name' : 'Celeb 1',
                'worth' : '3567892' 
            },

            {
                'name': 'Celeb 2',
                'worth': '23000000'
            },
            {
                'name': 'Celeb 3',
                'worth': '1000007'
            },
            {
                'name': 'Celeb 4',
                'worth': '456789'
            },
            {
                'name': 'Celeb 5',
                'worth': '7890000'
            },
            {
                'name': 'Celeb 6',
                'worth': '12000456'
            },
            {
                'name': 'Celeb 7',
                'worth': '896000'
            },
            {
                'name': 'Celeb 8',
                'worth': '670000'
            }
        ]
    }

    return render(request, 'data.html', context)
