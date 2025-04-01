from django.shortcuts import render

ice_cream_catalog = [
    {
        'id': 0,
        'title': 'Classic vanilla ice cream',
        'description': 'Real ice cream for true connoisseurs of taste. '
                       'If ice cream appears on the table, it won\'t last long.',
    },
    {
        'id': 1,
        'title': 'Grasshopper ice cream',
        'description': 'Topped with real '
                       'caramelized Colombian grasshoppers.',
    },
    {
        'id': 2,
        'title': 'Cheddar cheese ice cream',
        'description': 'The taste of real cheese in a wafer cup.',
    },
]


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    context = {'ice_cream': ice_cream_catalog[pk]}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {'ice_cream_list': ice_cream_catalog}
    return render(request, template, context)
