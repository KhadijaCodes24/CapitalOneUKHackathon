# FinanceSmart Hackathon — Budgeting Tracker

You are building a web app that helps a young adult track and manage their
monthly budget. A customer can log in, enter their income and outgoings,
view a breakdown of their spending, and receive suggestions on how to
improve their finances.

## THE BRIEF

Build a multi-page app with the following flow:

1. **Login page**
   An existing customer logs in with a username and password.

2. **Sign up page**
   A new customer creates an account.

3. **Dashboard**
   Shows the customer's name, email, and a summary of their budgets.
   Lists all budgets with the following columns:
     - Month / Year
     - Income
     - Carryover
     - Outgoings — the total actual spend across all categories for that budget
     - Spend Percentage — how much of the available money was spent, calculated as:

       ```
       spend_percentage = (total_outgoings / (monthly_income + carryover)) * 100
       ```

     - Date created and date last edited
   The customer can create a new budget, edit an existing one, or
   delete a past budget from this view.

4. **Budget entry page**
   The customer fills in their budget for a given month:
     - Monthly income — their total take-home pay for the month.
     - Outgoings — categorised spending across areas such as:
          rent, food, bills, hobbies, socialising, savings, etc.
     - Carryover — if the customer has an existing account, any
        savings or leftover balance from the previous month is
        pre-filled and can be adjusted before submission.

5. **Validation**
   Before the budget is saved, the backend checks that the total
   outgoings do not exceed the monthly income plus any carryover.

   ```
   total_outgoings ≤ monthly_income + carryover
   ```

6. **Results page**
   After a successful submission, the frontend displays:
     - A summary showing total expected vs actual spending and
        how much is remaining.
     - A per-category breakdown of expected vs actual amounts.
     - Suggestions on how to manage their spending better, based
        on the figures they have entered.

7. **Budget management**
   The customer can return to the dashboard at any time to:
     - Create a new monthly budget
     - Edit an existing budget (figures, categories, and carryover)
     - Delete a past budget they no longer need
   
   Every budget record stores the date it was created and the date
   it was last edited, both of which are visible on the dashboard.

## HTTP METHODS

Your backend will need to use the following HTTP methods:

- `GET` — retrieve data (e.g. load a budget, list all budgets)
- `POST` — create new data (e.g. save a new budget, login, register)
- `PATCH` — update existing data (e.g. edit a budget)
- `DELETE` — remove data (e.g. delete a budget)

The following are already implemented for you — use them as a reference:
```
POST   /login
POST   /logout
POST   /register
```

Some examples of methods you may want to implement are:
```
GET    /customer
GET    /budgets
POST   /budgets
GET    /budgets/<id>
PATCH  /budgets/<id>
DELETE /budgets/<id>
GET    /budgets/carryover
```

Example Flask route for each method:

```python
# GET — no request body, return data
@app.route("/example", methods=["GET"])
def example_get():
    return jsonify({"data": "here"}), 200

# POST — read body with request.get_json(), return 201 on creation
@app.route("/example", methods=["POST"])
def example_post():
    data = request.get_json()
    name = data.get("name")
    return jsonify({"message": f"Created {name}"}), 201

# PATCH — read body, update existing record, return 200
@app.route("/example/<int:item_id>", methods=["PATCH"])
def example_patch(item_id):
    data = request.get_json()
    # update the item with item_id using data
    return jsonify({"message": "Updated"}), 200

# DELETE — no body needed, just the id in the URL, return 200
@app.route("/example/<int:item_id>", methods=["DELETE"])
def example_delete(item_id):
    # delete the item with item_id
    return jsonify({"message": "Deleted"}), 200
```

## THE DATA

Demo accounts are pre-loaded for you:

```
Username: alice   Password: password123
Username: bob     Password: password123
```

- Alice's starting monthly income: £2800, Previous month carryover: £150
- Bob's starting monthly income:   £3500, Previous month carryover: £0

You are encouraged to create additional accounts.

## DATA STORAGE

By default the app uses CSV files (no install needed). If you want a stretch
goal, switch to SQLite by uncommenting the DB block in `app.py`.

CSV files provided:
- `users.csv` — customer login credentials
- `budgets.csv` — saved budgets per customer (starts with one demo budget each)
- `categories.csv` — spending categories per budget

SQLite (stretch goal):
- `schema.sql` — defines the 3 database tables (users, budgets, categories)
- `seed.py` — populates the database with the same demo data as the CSV files
- To use: uncomment the SQLite block in `app.py`, comment out the CSV block,
  then run: `python3 seed.py`

Note: CSV files are updated directly when budgets are saved — there is no
automatic reset. If a file gets corrupted or you want to start fresh, restore
it to its original values from the demo data above.

## WHAT YOU ARE GIVEN

- Working `/login`, `/logout`, and `/register` routes (use as your reference)
- Data helper functions — the following are complete and ready to use:
  `find_user`, `find_user_by_id`, `_read_csv`, `_write_csv`, `_next_id`, `_save_categories`

  The following are stubbed with TODOs for you to implement:
  `get_budgets_for_user`, `get_budget_by_id`, `get_categories_for_budget`,
  `get_latest_budget`, `save_budget`, `update_budget`, `delete_budget`, `register_user`
- Most frontend pages stubbed with HTML comments
- `login.html` and `login.js` fully built as a reference — no changes needed
- `app.js`, `budget.js`, and `signup.js` stubbed with TODOs
- `calculator.py` stubbed — you implement the maths and validation logic
- Two fully worked example test files are provided (both self-contained —
  they define their own helper functions and don't depend on your `app.py` code):
  `test_csv_io.py` — tests for reading and writing CSV files
  `test_data.py` — tests for common SQLite query patterns (find, save, delete)
- One stubbed test file for you to complete as a stretch goal:
  `test_calculator.py` — test method names and function calls are written,
  you write the assert statements
- `seed.py`, `schema.sql`, and all CSV files pre-populated

## WHAT YOU NEED TO BUILD

**Backend:**
- Implement `calculate_budget_summary()` in `calculator.py`
- Implement `validate_budget()` in `calculator.py`
- Implement `generate_suggestions()` in `calculator.py`
- Implement the data functions (`get_budgets_for_user`, `save_budget`, etc.)
- Complete the `/customer`, `/budgets`, and `/budgets/<id>` routes

**Frontend:**
- Design and build `index.html` (dashboard), `budget.html` (entry/results) and `signup.html` (user registration)
- Complete `app.js`, `budget.js`, and `signup.js`

**Tests:**
- Complete the assertions in `test_calculator.py` and add any extra test cases you think may be needed (stretch goal)

## PAGES AND DESIGN

The design and layout is yours to create. You are also free to add more
pages or split existing pages if it makes sense for your design — for
example, you could have a separate results page instead of showing results
on the same page as the form.

If you do any planning electronically (wireframes, diagrams, docs), add the
links to `GROUP_LINKS.txt` so assessors can access them. Pen and paper is fine
too — just hand it in at the end.

## EXTENSIONS (stretch goals)

- **Testing**: complete the assertions in `test_calculator.py` and add any other additional testing you think may be needed
- **Input validation**: add validation and user-friendly error messages throughout
  (`login.js` shows a worked example of handling success/error responses — use it as a reference)
- **Database**: switch from CSV to SQLite (uncomment the DB block in `app.py`)

## HOW TO RUN

```bash
cd backend
pip install -r requirements.txt
python3 app.py
```

Open the frontend (run from inside the `budgeting/` folder):
```bash
python3 -m http.server 8080
```
Open: http://localhost:8080/frontend/login.html

Run tests:
```bash
cd backend && python3 -m pytest
```

