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

---

## Notes

- [x] Create note
- [x] Edit own notes
- [x] Delete own notes
- [x] Allow DM to delete all notes
- [x] View notes
- [x] Automatically assign `created_by`
- [x] Sort notes (Latest / Oldest)
- [x] Search notes by title
- [x] Keep search and sorting combined
- [x] Display creation date in note header

---

## User Interface

- [x] Responsive Bootstrap layout
- [x] Dynamic sidebar
- [x] Context-aware navigation
- [x] Dashboard split into owned/member campaigns
- [x] Collapsible note folders per user
- [x] Modern note cards
- [x] Notes toolbar (Search + Sort + New Note)

---

# Current Tasks

## Campaign Members

- [ ] Prevent duplicate members
- [ ] Prevent adding campaign owner
- [ ] Display useful error when username doesn't exist
- [ ] Remove members

---

## Note Permissions

- [ ] Allow campaign members to create notes
- [ ] Allow campaign members to edit only their own notes
- [ ] Allow campaign members to view notes

---

## Note Visibility

- [ ] Private notes visible to:
    - [ ] Note owner
    - [ ] Dungeon Master

- [ ] Public notes visible to:
    - [ ] Campaign members

- [ ] Filter notes by visibility

---

# Future Improvements

## Search & Filtering

- [ ] Search campaign names
- [ ] Search note content
- [ ] Filter by visibility
- [ ] Filter by creator
- [ ] Filter by creation date

---

## User Experience

- [ ] Django messages framework
- [ ] Empty search result message
- [ ] User profile page
- [ ] Dashboard statistics

---

## Notes

- [ ] Categories
- [ ] Tags
- [ ] Rich text editor
- [ ] File attachments

---

## Campaigns

- [ ] Invite users
- [ ] Multiple Dungeon Masters