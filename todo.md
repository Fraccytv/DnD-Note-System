# TODO

## Completed

### Authentication

* [x] User registration
* [x] User login
* [x] User logout
* [x] Landing page for guests
* [x] Dashboard for authenticated users
* [x] Protect authenticated views with `LoginRequiredMixin`
* [x] Redirect unauthenticated users to the login page

### Campaigns

* [x] Create campaign
* [x] View owned campaigns
* [x] View campaigns where the user is a member
* [x] Open campaign
* [x] Delete campaign
* [x] Delete confirmation dialog
* [x] Assign `created_by` automatically when creating a campaign
* [x] Show only campaigns owned by the logged-in user
* [x] Prevent users from accessing other users' campaigns
* [x] Allow campaign members to open a campaign

### Campaign Members

* [x] Add members to campaigns
* [x] Show campaign members
* [x] Display DM separately from campaign members
* [x] Dashboard section for campaigns you're a member of

### Notes

* [x] Create note
* [x] View notes
* [x] Edit note
* [x] Delete note
* [x] Assign `created_by` automatically when creating a note
* [x] Prevent users from editing/deleting notes they do not own

### User Interface

* [x] Responsive Bootstrap layout
* [x] Dynamic sidebar
* [x] Context-aware navigation (New Campaign / New Note)
* [x] Welcome message for logged-in users
* [x] Dashboard separated into "Your Campaigns" and "Campaigns You're a Member Of"

---

## Chatgpt explain:
joh det kan det vel godt være men hvorfor skal jeg så have 
        is_dm = campaign.created_by == request.user
        is_member = campaign.members.filter(id=request.user.id).exists()

        if not (is_dm or is_member):
            return redirect("home")????

Det er et mega godt spørgsmål. Og her er det vigtigt at skille to ting ad.

Du blander lige nu:

Må brugeren oprette en note? (adgangskontrol)
Hvem ejer noten? (data)

Det er to forskellige problemer.

Problem 1 - Må brugeren være her?

Det er det, denne kode afgør:

is_dm = campaign.created_by == request.user
is_member = campaign.members.filter(id=request.user.id).exists()

if not (is_dm or is_member):
    return redirect("home")

Den spørger:

"Har denne bruger overhovedet lov til at oprette en note?"

Hvis svaret er nej...

Random bruger
    ↓
Prøver at gå til:
/note/4/
    ↓
Bliver sendt tilbage
Problem 2 - Hvem ejer noten?

Når brugeren har fået lov til at være der, skal vi gemme noten.

Hvem har skrevet noten?

Den bruger, der er logget ind.

Derfor:

note.created_by = request.user

Det har intet med is_dm eller is_member at gøre.

Tænk på det som en natklub 😄

Der står en dørmand.

Først spørger dørmanden:

Er du på gæstelisten?

Det svarer til:

is_dm
is_member

Hvis nej:

Du kommer ikke ind.

Hvis ja:

Du kommer ind.

Nu køber du en øl.

Hvem købte øllen?

Det gjorde dig.

Ikke dørmanden.

Ikke ejeren af natklubben.

Derfor:

note.created_by = request.user

Så de to ting har to helt forskellige formål:

# Adgang
is_dm = ...
is_member = ...

if not (...):
    ...

og

# Ejerskab
note.created_by = request.user

De hænger ikke sammen, selvom de står i samme view.

💡 Lille bonus: Det er faktisk en af de vigtigste ting, man lærer som backend-udvikler:

Authorization (må brugeren gøre det?)
Data (hvad skal gemmes i databasen?)

Det er to forskellige ansvarsområder, og det er derfor, vi holder dem adskilt. Det er også derfor, jeg hele tiden spørger dig: "Hvad prøver denne kode egentlig at opnå?" Det hjælper med at holde logikken ren og nem at forstå.

##


# Next Tasks

## Campaign Members

* [ ] Prevent adding duplicate members
* [ ] Prevent adding non-existing users gracefully
* [ ] Prevent adding the campaign owner
* [ ] Remove campaign members
* [ ] Invite users to campaigns (future)

## Campaign Permissions

* [ ] Allow campaign members to create notes
* [ ] Allow campaign members to view notes
* [ ] Keep campaign owner as the DM
* [ ] Prepare support for multiple DMs in the future

## Note Visibility

* [ ] Private notes visible only to:
  * [ ] Note owner
  * [ ] Campaign owner (DM)

* [ ] Public notes visible to:
  * [ ] All campaign members

* [ ] Filter notes based on visibility

## Sharing

* [ ] Public/private note workflow
* [ ] Campaign collaboration

---

# Future Improvements

* [ ] Username autocomplete when adding members
* [ ] Search campaigns
* [ ] Search notes
* [ ] Dashboard statistics
* [ ] Success and error messages (`messages` framework)
* [ ] User profile page
* [ ] Note categories/tags
* [ ] File attachments
* [ ] Rich text editor
* [ ] Multiple DMs per campaign