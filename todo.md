# TODO

---

# Completed

## Authentication

- [x] User registration
- [x] User login
- [x] User logout
- [x] Landing page for guests
- [x] Dashboard for authenticated users
- [x] Protect authenticated views with `LoginRequiredMixin`
- [x] Redirect unauthenticated users to the login page

---

## Campaigns

- [x] Create campaign
- [x] View owned campaigns
- [x] View campaigns where the user is a member
- [x] Open campaign
- [x] Delete campaign
- [x] Delete confirmation dialog
- [x] Automatically assign `created_by`
- [x] Restrict access to campaign owner and members

---

## Campaign Members

- [x] Add members
- [x] Display campaign members
- [x] Display Dungeon Master separately
- [x] Show member campaigns on dashboard
- [x] Prevent duplicate members
- [x] Prevent adding campaign owner
- [x] Display useful error when username doesn't exist
- [x] Remove members
- [x] Remove member confirmation modal

---

## Notes

- [x] Create note
- [x] Edit own notes
- [x] Delete own notes
- [x] Allow DM to delete all notes
- [x] View notes
- [x] Automatically assign `created_by`
- [x] Sort notes (Latest / Oldest)
- [x] Search notes by title and content
- [x] Keep search and sorting combined
- [x] Display creation date in note header

---

## User Interface

- [x] Responsive Bootstrap layout
- [x] Dynamic sidebar
- [x] Context-aware navigation
- [x] Dashboard split into owned/member campaigns
- [x] Collapsible note folders per user
- [x] Show only users with visible notes
- [x] Modern note cards
- [x] Notes toolbar (Search + Sort + New Note)

---

## Note Permissions

- [x] Allow campaign members to create notes
- [x] Allow campaign members to edit only their own notes
- [x] Allow campaign members to view notes

---

## Note Visibility

- [x] Private notes visible to:
    - [x] Note owner
    - [x] Dungeon Master

- [x] Public notes visible to:
    - [x] Campaign members

---


## Search & Filtering

- [x] Search campaign names
- [x] Search descriptions and Dungeon Master

---

## User Experience

- [x] Django messages framework
- [x] Remember expanded note folders after page reload
- [x] Empty search result message

---

# Current Tasks

## Notes
- [ ] Markdown support
- [ ] Markdown preview