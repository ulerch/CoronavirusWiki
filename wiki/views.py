from django.shortcuts import render, redirect
from .models import Register, Row, Column, WikiEntry
from .forms import CreateForm


def wikiMatrix(request, regPk=None):
    context = {}
    if regPk is None:
        regPk = Register.objects.first().pk

    context['active_reg'] = regPk
    context['regs'] = Register.objects.all()
    context['cols'] = Column.objects.filter(register=regPk)
    context['rows'] = Row.objects.filter(register=regPk)

    return render(request, 'wiki/index.html', context)


def wikiList(request, rowPk, colPk):
    context = {}
    context['row'] = rowPk;
    context['col'] = colPk;
    context['title'] = Row.objects.get(pk=rowPk).label + ' - ' + Column.objects.get(pk=colPk).label
    context['entries'] = WikiEntry.objects.filter(row=rowPk, column=colPk)

    return render(request, 'wiki/list.html', context)


def wikiCreateView(request, rowPk, colPk):
    context = {}
    context['row'] = rowPk
    context['col'] = colPk
    context['title'] = Row.objects.get(pk=rowPk).label + ' - ' + Column.objects.get(pk=colPk).label

    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            #instance = form.save(commit=False)
            f_title = form.cleaned_data.get('title')
            f_text = form.cleaned_data.get('text')
            f_name = form.cleaned_data.get('name')
            f_email = form.cleaned_data.get('email')
            f_row = Row.objects.get(pk=rowPk)
            f_column = Column.objects.get(pk=colPk)
            new = WikiEntry(
                row = f_row,
                column = f_column,
                title = f_title,
                text = f_text,
                contributor_name = f_name,
                contributor_email = f_email,
            )
            new.save()
            return redirect("/")
    else:
        form = CreateForm()

    return render(request, 'wiki/create.html', {'form': form, 'context': context})
