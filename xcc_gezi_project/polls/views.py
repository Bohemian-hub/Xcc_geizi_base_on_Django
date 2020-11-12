from django.http import HttpResponse, Http404  # 可以返回渲染的页面
from django.shortcuts import render

from .models import Meishi, Question  # 导入我们的模型类


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


# 添加数据方法
def add_food(request):
    # 第一种方式插入数据
    tcpg = Meishi(food_name='糖醋排骨', food_author='一一', food_money=25, food_star='美味')
    tcpg.save()  # 一定要记得保存，不然数据无法插入进去
    # 第二种方式插入数据
    lzj = Meishi()
    lzj.food_name = '辣子鸡'
    lzj.food_author = '张三'
    lzj.food_money = '30'
    lzj.food_star = '超级美味'
    lzj.save()  # 一定要记得保存，不然数据无法插入进去
    # 第三种方式插入数据（该方法不需要保存，会自动保存）
    sltds = Meishi.objects.create(food_name='酸辣土豆丝', food_author='一一', food_money=25, food_star='美味')
    # 第四种方式插入数据（该方法不需要保存，且不会插入重复数据）
    clbc = Meishi.objects.get_or_create(food_name='醋溜白菜', food_author='李四', food_money=25, food_star='很美味')
    return HttpResponse("添加数据成功")


# 查询数据方法
def select_food(request):
    # 查询表中的所有数据
    rs = Meishi.objects.all()
    print(rs)
    # 根据筛选条件查询出表中的单挑数据（注意如果条件查询出多条数据，使用该语句会报错）
    rs1 = Meishi.objects.get(food_name='醋溜白菜')
    print(rs1)
    # 根据筛选条件查询出表中的数据（可查询出多条）
    rs2 = Meishi.objects.filter(food_author="一一")
    rs2 = list(rs2)
    print(rs2)
    return HttpResponse("查询数据成功")


# 更新数据方法
def update_food(request):
    # 根据条件查询后再修改再保存
    clbc = Meishi.objects.get(food_name='醋溜白菜')
    clbc.food_star = '难吃'
    clbc.save()
    # 直接修改所有的数据
    Meishi.objects.all().update(food_star='美味')
    return HttpResponse("修改数据成功")


# 删除数据方法
def delete_food(request):
    Meishi.objects.get(id=4).delete()
    return HttpResponse("删除数据成功")
