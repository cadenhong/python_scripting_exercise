'''
Sales Season
A retailer is having a store-wide "buy 2, get 1 free" sale. For legal reasons, they can't charge their customers $0 for an article so a discount is applied to all products instead.

For example, if a customer gets three products a, b and c:
Product A Product B Product C
$15.99 $23.50 $10.75

She gets the cheapest one for free, so she ends up paying $15.99 + $23.50 = $39.49, but what her receipt says is:
Product A: $15.99 − Special Discount = $12.57
Product B: $23.50 − Special Discount = $18.47
Product C: $10.75 − Special Discount = $8.45
Total: $39.49

Create a function that takes in a list of prices for a customer's shopping cart and returns the prices with the discount applied. Round all prices to the cent.

Examples
discount([2.99, 5.75, 3.35, 4.99]) ➞[2.47, 4.74, 2.76, 4.12] # First product for free.
discount([10.75, 11.68]) ➞ [10.75, 11.68] # No discounts applied.
discount([68.74, 17.85, 55.99]) ➞ [60.13, 15.62, 48.98] # Second product for free.
discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]) ➞ [5.16, 13.45, 33.06, 10.91, 22.71, 5.16, 5.16, 5.16] # First and sixth products for free (see second note).

Notes
The discount is calculated in percentual terms.
The deal applies to sets of three products: if a customer gets 9 products, she will get the three cheapest ones for free, but if she gets 10 or 11 products, she will still get three for free. Buying a 12th product would get her a fourth free product.
No cart splitting allowed.
'''

def discount(shopping_cart):
    if int(len(shopping_cart)) < 3:
        return shopping_cart
    else:
        sorted_cart = sorted(shopping_cart) # new list ordered from smallest -> largest
        discount_qualified_items = len(shopping_cart) // 3  # num of items that ARE qualified for discount (aka free)
        discount_total = 0
        for i in range(discount_qualified_items):   # total amount to be discounted
            discount_total += sorted_cart[i]

        new_shopping_cart = []
        total_bill = sum(shopping_cart) # entire bill BEFORE discount
        for j in shopping_cart:
            percentage = j / total_bill # ratio of item compared to total bill, to be used to calculate discount
            new_shopping_cart.append(round((j - (discount_total * percentage)), 2)) # append to new shopping cart, round to 2 decimal places

        return new_shopping_cart


print(discount([2.99, 5.75, 3.35, 4.99]))
print(discount([10.75, 11.68]))
print(discount([68.74, 17.85, 55.99]))
print(discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]))


'''
Sample Code:

def discount(lst):
    per = sum(sorted(lst)[len(lst)//3:])/sum(lst)
    return [round(price*per, 2) for price in lst]
'''