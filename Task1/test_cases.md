# SDET Assessment Bingyan Chen

## Task 1

*Priority level (1 for the most priority, 5 for the least priority)*

1. [Go-Shopping] [Add-Item] Product page and Add item

   - Test Case ID: GoShop_AddItem_01
   - Priority level: 1

   - Description: Verify redirection to product page and add item to cart
   - Steps:
     - Open the website Jupiter Toys
     - Click start shopping button
     - Click Buy Button for Teddy Bear once
     - Click Buy Button for Stuffed Frog once
     - Click Buy Button for Handmade doll once
     - Click Buy Button for Fluffy Bunny once
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - 1 (one) Handmade doll is correctly added to cart
     - 1 (one) Fluffy Bunny is correctly added to cart
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - 1 (one) Handmade doll is correctly added to cart
     - 1 (one) Fluffy Bunny is correctly added to cart
   - Status: Pass

2. [Go-Shopping] [Add-Item] Product page and Add item

   - Test Case ID: GoShop_AddItem_02
   - Priority level: 1
   - Description: Verify redirection to product page and add item to cart
   - Steps:
     - Open the website Jupiter Toys
     - Click start shop button in header section
     - Click Buy Button for Teddy Bear once
     - Click Buy Button for Stuffed Frog once
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
   - Status: Pass

3. [Go-Shopping] [Add-Item] [Attempt-Check-Out] Product page, Add item and Attempt to checkout

   - Test Case ID: GoShop_AddItem_AttemptCheckout_01
   - Priority level: 2
   - Description: Verify redirection to product page,  add item to cart and redirection to Payment and Delivery Page
   - Steps:
     - Open the website Jupiter Toys
     - Click Cart in header section and click Start Shopping button
     - Click Buy Button for Teddy Bear once
     - Click Buy Button for Stuffed Frog once
     - Click Cart in the header section
     - Click Green CheckOut button
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
   - Status: Pass

4. [Go-Shopping] [Add-Item] [Attempt-Check-Out] Product page, Add item and Attempt to checkout

   - Test Case ID: GoShop_AddItem_AttemptCheckout_02
   - Priority level: 2
   - Description: Verify redirection to product page,  add item to cart and redirection to Payment and Delivery Page
   - Steps:
     - Open the website Jupiter Toys
     - Click Cart in header section and click Start Shopping button
     - Click Buy Button for Teddy Bear once
     - Click Buy Button for Stuffed Frog once
     - Click Cart in the header section
     - Click CheckOut Text with hyperlink
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
   - Status: Pass

5. [Go-Shopping] [Add-Item] [Attempt-Check-Out] [Check-Out] Product page, Add item, Attempt to checkout and Checkout with mastercard

   - Test Case ID: GoShop_AddItem_AttemptCheckout_Checkout_01
   - Priority level: 1
   - Description: Verify redirection to product page,  add item to cart, redirection to Payment and Delivery Page, and Checkout with valid mastercard number 
   - Steps:
     - Open the website Jupiter Toys
     - Click Cart in header section and click Start Shopping button
     - Click Buy Button for Teddy Bear once
     - Click Buy Button for Stuffed Frog once
     - Click Cart in the header section
     - Click CheckOut Text with hyperlink
     - Fill valid Delivery Details
     - Select mastercard for card type, and enter a valid mastercard number
     - Click the Checkout button
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
     - Delivery details accepted
     - Payment details accepted
     - Order processed correctly
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
     - Delivery details accepted
     - Payment details accepted
     - Order processed correctly
   - Status: Pass

6. [Go-Shopping] [Add-Item] [Attempt-Check-Out] [Check-Out] Product page, Add item, Attempt to checkout and Checkout with Visa

   - Test Case ID: GoShop_AddItem_AttemptCheckout_Checkout_02
   - Priority level: 1
   - Description: Verify redirection to product page,  add item to cart, redirection to Payment and Delivery Page, and Checkout with valid Visa number 
   - Steps:
     - Open the website Jupiter Toys
     - Click Cart in header section and click Start Shopping button
     - Click Buy Button for Teddy Bear once
     - Click Buy Button for Stuffed Frog once
     - Click Cart in the header section
     - Click CheckOut Text with hyperlink
     - Fill valid Delivery Details
     - Select Visa for card type, and enter a valid Visa card number
     - Click the Checkout button
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
     - Delivery details accepted
     - Payment details accepted
     - Order processed correctly
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - 1 (one) Stuffed Frog is correctly added to cart
     - The website is redirected to the cart page
     - The website is redirected to the Delivery and Payment page
     - Delivery details accepted
     - Payment details accepted
     - Order processed correctly
   - Status: Pass

7. [Empty-Cart] Add item and Empty Cart

   - Test Case ID: EmptyCart_01
   - Priority level: 1
   - Description: Add item and then empty cart
   - Steps:
     - Open the website Jupiter Toys
     - Click start shopping button
     - Click Buy Button for Teddy Bear once
     - Click Cart in the header section
     - Click the Empty Cart button
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - The website is redirected to the cart page
     - The Cart is emptied successfully.
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - The website is redirected to the cart page
     - The Cart is emptied successfully.
   - Status: Pass

8. [Edit-item-quantity] 

   - Test Case ID: EditItem_01
   - Priority level: 1
   - Description: Verify editing item quantity in cart
   - Steps:
     - Open the website Jupiter Toys
     - Click start shopping button
     - Click Buy Button for Teddy Bear once
     - Click Cart in the header section
     - Edit quantity for Teddy Bear to 2
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - The website is redirected to the cart page
     - The quantity on cart is updated correctly, the desciptive text in the top of the cart is updated correctly, and subtotal and total unpaid is updated correctly.
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the shopping page
     - 1 (one) Teddy Bear is correctly added to cart
     - The website is redirected to the cart page
     - The quantity on cart is updated correctly, the desciptive text in the top of the cart is updated correctly, and subtotal and total unpaid is updated correctly.
   - Status: Pass

9. [Contact] Contact functionality

   - Test Case ID: Contact_01
   - Priority level: 3
   - Description: Verify Contact functionality
   - Steps:
     - Open the website Jupiter Toys
     - Click Contact in the header section
     - Fill the required information
     - Click Submit button
   - Expected Behaviours:
     - The website is opened successfully and correctly
     - The website is redirected to the contact page
     - The information is accepted successfully
     - The ticket is submitted successfully
   - Actual Behaviours: 
     - The website is opened successfully and correctly
     - The website is redirected to the contact page
     - The information is accepted successfully
     - The ticket is submitted successfully
   - Status: Pass

10. [Login] Login functionality

    - Test Case ID: Login_01
    - Priority level: 2
    - Description: Verify Login functionaility
    - Steps:
      - Open the website Jupiter Toys
      - Click Login in the header section
      - Input valid credentials and click login
    - Expected Behaviours:
      - The website is opened successfully and correctly
      - Login dialog pop up
      - Credentials accpeted and login successfully.
    - Actual Behaviours: 
      - The website is opened successfully and correctly
      - Login dialog pop up
      - Login failed
    - Status: Fail