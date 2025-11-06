from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo

# Function based view
def todo_list(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    return render(request, 'Todo/todo_list.html', context)

# Class based views
class TodoListView(ListView):
    model = Todo
    template_name = 'Todo/todo_list.html'
    context_object_name = Todo
    
class TodoCreateView(CreateView):
    model = Todo
    template_name = 'Todo/todo_create.html'
    success_url = reverse_lazy('todo-list')

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'Todo/todo_update.html'
    success_url = reverse_lazy('todo-list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'Todo/todo_delete.html'
    success_url = reverse_lazy('todo-list')

# Function for toggling completed
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo-list')