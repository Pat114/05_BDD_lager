from behave import given, when, then
from src.lager import Stock, StockItem

@given(u'att lagret är tomt')
def step_impl(context):
    context.stock = Stock()
    
@when(u'när jag lägger dit 10 st äpplen')
def step_impl(context):
    product = StockItem ("Äpplen", 10)
    context.stock.add_product(product)  
        
@then(u'ska produkten heta Äpplen')
def step_impl(context):
    assert context.stock.items[0].name == "Äpplen"
        
@then(u'ska lagret vara 10 st')
def step_impl(context):
    assert context.stock.items[0].amount == 10
     
@given(u'att lagret innehåller 10 st Äpplen')
def step_impl(context):
    context.stock = Stock()
    context.product = StockItem("Äpplen", 10)
    context.stock.add_product(context.product)            
        
@when(u'jag tar bort 3 st Äpplen')
def step_impl(context):
    context.stock.remove_product(context.product, 3)
            
@then(u'ska lagret vara 7 st')
def step_impl(context):
    assert context.product.amount == 7
    
@when(u'jag lägger dit 5 st bananer')
def step_impl(context):
    context.product = StockItem ("bananer", 5)
    context.stock.add_product(context.product)
    
@then(u'ska produkten heta bananer')
def step_impl(context):
    assert context.product.name == 'bananer'

@then(u'lagret vara 5 st')
def step_impl(context):
    assert context.product.amount == 5
    