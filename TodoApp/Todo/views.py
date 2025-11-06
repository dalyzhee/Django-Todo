from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

# Function based view
def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'Todo/todo_list.html', context)

# Class based views
class TodoListView(ListView):
    model = Todo
    template_name = 'Todo/todo_list.html'
    context_object_name = 'Todo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['completed_count'] = Todo.objects.filter(completed=True).count()
        return context
    
class TodoCreateView(CreateView):
    model = Todo
    #fields = ['title']
    form_class = TodoForm
    template_name = 'Todo/todo_create.html'
    success_url = reverse_lazy('todo-list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title']
    template_name = 'Todo/todo_confirm_update.html'
    success_url = reverse_lazy('todo-list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'Todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo-list')

# Function for toggling completed
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo-list')