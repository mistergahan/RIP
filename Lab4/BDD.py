from radish import given, when, then


@given("I have the component {component1: g}")
def have_component(step, component1):
    step.context.component1 = component1


@when("I get price from them")
def get_price_component(step):
    step.context.result = step.context.component1.get_price()


@then("I expect the result to be {result: g}")
def expect_result(step, result):
    assert step.context.result == result
