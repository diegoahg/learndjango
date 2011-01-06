from django.shortcuts import render_to_response
from learndjango.poketest.models import *

def ajax_create_poke_info(request):
    name = request.POST['poke_name']
    return ''

def pokedex_show(request):
    pokedex_entries = PokeInfo.objects.all()
    params = {
        'pokemon': pokedex_entries,
    }
    return render_to_response('index_pokedex.html', params)

def pokedex_lookup(request, name):
    pokemon = PokeInfo.objects.get(name__iexact=name)
    params = { 
        'pokemon' : {
            'name' : pokemon.name,
            'sprite' : {
                'row': pokemon.sprite.row,
                'col':  pokemon.sprite.col,
            },
        },
    }
    return render_to_response('pokedex.html', params)
