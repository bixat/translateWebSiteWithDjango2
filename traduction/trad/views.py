from django.shortcuts import render
# Create your views here.
from trad.forms import trd
from mydb import verf

def trad(request):
    frm = trd(request.POST)
    if frm.is_valid():
        w = request.POST['word']
        wr = verf(w)
        return render(request, 'index.html', {'frm': frm,'wrd':wr})
    else:
        return render(request, 'index.html', {'frm': frm})