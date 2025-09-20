# Bulk Unlock Sales Orders

Unlock multiple locked Sales Orders in one go from the Sales Orders list view.

---

## Features

- Adds an **Action ▸ Unlock Sales Orders** option in the Sales Orders list view.
- Select several locked orders at once and unlock them in bulk.
- Respects standard Odoo access rights and workflow.

---

## Compatibility

- Odoo: 16.0 / 17.0 / 18.0 (adjust if different)

---

## Dependencies

- `sale`
- `sale_management`

---

## Installation

1. Copy this module into your Odoo `addons` path.
2. Update the app list: **Apps ▸ Update Apps List**.
3. Install **Bulk Unlock Sales Orders**.

---

## Usage

1. Go to **Sales ▸ Orders**.
2. Switch to the **list** (tree) view.
3. Select the locked Sales Orders you want to unlock.
4. Click **Action ▸ Unlock Sales Orders**.
5. The selected Sales Orders will be unlocked immediately.

> Notes:
> - Only orders in the **Locked** state will be unlocked.
> - Orders already unlocked remain unchanged.
> - Standard Odoo permissions apply.

---

## Access Rights

- Users need Sales Orders access rights (`sale_user` or above).
- The bulk action is only available for users allowed to unlock orders individually.

---

## Known Limitations

- Quotations or already unlocked orders are skipped.
- Custom workflows or third-party modules may alter behavior.

---

## Support & Issues

If you encounter problems or want enhancements, please open an issue or contact the developer.

---

## Author

- **Manish Kumar Bohra**

## Developer

- **Manish Kumar Bohra** — <manishkumarbohra@outlook.com>

---

## License

This module is licensed under the same terms as Odoo Community addons unless specified otherwise. Update this section if you use a different license.
