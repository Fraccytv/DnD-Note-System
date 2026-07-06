# D&D Note System

A web application built with Django for managing Dungeons & Dragons campaigns and notes.

---

## Tech Stack

* Python
* Django 6
* SQLite
* Bootstrap 5
* Class Based Views (CBV)
* ModelForms

---

# Features

## Authentication

* ✅ User registration
* ✅ User login
* ✅ User logout
* ✅ Landing page for guests
* ✅ Dashboard for authenticated users
* ✅ Sidebar changes depending on login status
* ✅ Welcome message displaying the logged-in username

---

## Campaigns

Users can:

* ✅ Create campaigns
* ✅ View all campaigns
* ✅ Open a campaign
* ✅ Delete a campaign
* ✅ Confirmation dialog before deleting

---

## Notes

Users can:

* ✅ Create notes inside a campaign
* ✅ View all notes for a campaign
* ✅ Edit notes
* ✅ Delete notes

---

## User Interface

* Dark Bootstrap 5 dashboard
* Responsive layout
* Campaign cards
* Landing page for guests
* Dashboard for authenticated users
* Dynamic sidebar navigation
* Context-aware navigation:

  * Dashboard → **New Campaign**
  * Campaign pages → **New Note**

---

## Current Project Structure

```text
templates/
    base.html

notes/
    templates/
        notes/
            home.html
            campaign_detail.html
            make_campaign.html
            make_notes.html
            edit_note.html

registration/
    login.html
    register.html
```

---

# Implemented Views

* MainView
* MakeCampaignView
* CampaignDetailView
* MakeNoteView
* EditNoteView
* DeleteNoteView
* DeleteCampaignView
* RegisterView
* LoginView
* LogoutView

---

# Implemented Models

## Campaign

* name
* description

## Note

* campaign (ForeignKey → Campaign)
* title
* content
* created_by
* created_at
* updated_at
* visibility (Public / Private)

---

# What I Have Learned

* Django project structure
* Models
* ForeignKey relationships
* ModelForms
* Class Based Views
* GET vs POST requests
* Redirect after POST (PRG Pattern)
* Django Templates
* Bootstrap 5
* URL parameters
* CRUD operations
* Authentication
* Login / Logout flow
* User registration
* CSRF protection
* JavaScript `confirm()` dialogs
* Conditional template rendering with `user.is_authenticated`
* Context-aware navigation

---

# Planned Features

## User Ownership

* Store campaign owner
* Automatically assign `created_by` on notes
* Automatically assign campaign owner

---

## Permissions

* Only owners can edit campaigns
* Only owners can delete campaigns
* Only owners can edit notes
* Only owners can delete notes

---

## Campaign Visibility

* Show only campaigns owned by the logged-in user
* Hide campaigns from guests
* Display only notes the user has permission to view

---

## Sharing

* Share notes with selected users
* Campaign members
* Shared campaigns
* Public / Private notes

---

## Quality Improvements

* LoginRequiredMixin
* Permission checks
* Better validation
* Success/error messages
* User profile menu
* Improved dashboard statistics
* Search functionality
* Note categories/tags
* Rich text support (optional)
* File attachments (optional)

---

# Current Status

The application is fully functional as a basic CRUD system with authentication.

Users can:

* Register
* Login
* Logout
* Create campaigns
* Create notes
* Edit notes
* Delete notes
* Delete campaigns
* Navigate through a responsive Bootstrap interface

The next milestone is implementing ownership and permission-based access control so that users only see and manage their own campaigns and notes.
