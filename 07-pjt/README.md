# 07-pjt

## Problem A

힘들었던 경우가 세가지 있었습니다.

첫 번째는 옵션 테이블에서 fin_prdt_cd에 계속 값이 들어오지 않는 현상이 있었습니다. DepositOptionsSerializer의 read_only_fields에 fin_prdt_cd가 들어가 있어 생긴 오류로 받을 때문 주석을 처리해서 해결했습니다.

두 번째는 재 호출시 에러 메시지가 나오는 현상입니다. 이 현상은 DepositProducts의 fin_prdt_cd가 unique여서 생겼던 거였고 try-except문을 활용해서 예외 처리를 했습니다.

```python
try:
    if serializer.is_valid(raise_exception=True):
        serializer.save()
except:
    pass
```

## Problem B

DepositProducts.objects.all()을 사용해서 데이터들을 가져온 다음 serializer로 감싸서 return하기만 하면 되서 어렵지 않게 해결했습니다.

## Problem C

request를 통해 넘어온 데이터를 serializer로 만드는것이 햇갈렸던 것을 제외하고는 어렵지 않게 해결했습니다.

## Problem D

filter()를 사용해서 옵션 리스트를 만들고 serializer에 감싸서 return하기만 하면 되서 어렵지 않게 해결할 수 있었습니다.

## Problem E

금리가 가장 높은 상품을 건져내는건 어렵지 않게 해결할 수 있었습니다. 하지만 해당 상품과 옵션 리스트를 묶어서 반환하는것에 어려움이 있었는데 dict에 값을 담아서 보낼 때 내부까지 dict, list등으로 변환해야 했습니다. 그래서 `__dict__`를 사용해서 객체를 dict로 변환 후 이를 새 dict에 담아서 해결했습니다.

```python
top_rate_option_dict_list = []
top_rate_product_dict = top_rate_product.__dict__
top_rate_product_dict.pop('_state', None)

for option in top_rate_option_list:
    option_dict = option.__dict__
    option_dict.pop('_state', None)
    top_rate_option_dict_list.append(option_dict)
    
print(top_rate_product_dict)
print(top_rate_option_dict_list)
    
ret = {
    'deposit_product': top_rate_product_dict,
    'option': top_rate_option_dict_list,
}

```