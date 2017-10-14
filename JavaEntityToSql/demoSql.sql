SELECT details.id,
		details.source_no,
		details.source_line_no,
		details.source_type,
		details.qty,
		details.process_qty,
		details.unit,
		details.mat_price,
		details.mat_wastage_rate,
		details.mat_rec_qty,
		details.mat_wastage_qty,
		details.pur_qty,
		details.pur_price,
		details.pur_unit,
		details.memo,
		details.lot_no,
		details.lock_for,
		details.lock_by,
		details.status,
		details.create_hr_id,
		details.update_hr_id,
		heads.name AS inv_mat_bill_head__name,
		details.inv_mat_bill_head_id AS inv_mat_bill_head__id,
		materials.name AS material__name,
		details.material_id AS material__id,
		centers.name AS inv_cost_center__name,
		details.inv_cost_center_id AS inv_cost_center__id,
		accounts.name AS inv_account__name,
		details.inv_account_id AS inv_account__id,
		organizations.name AS organization__name,
		details.organization_id AS organization__id,
		inventories.name AS inv_inventory__name,
		details.inv_inventory_id AS inv_inventory__id,
		locations.name AS inv_location__name,
		details.inv_location_id AS inv_location__id,
		addresses.name AS inv_address__name,
		details.inv_address_id AS inv_address__id
 FROM inv_mat_bill_details AS details LEFT JOIN inv_mat_bill_heads AS heads ON heads.id = details.inv_mat_bill_head_id
		 LEFT JOIN inv_materials AS materials ON materials.id = details.material_id
		 LEFT JOIN inv_cost_centers AS centers ON centers.id = details.inv_cost_center_id
		 LEFT JOIN inv_accounts AS accounts ON accounts.id = details.inv_account_id
		 LEFT JOIN inv_organizations AS organizations ON organizations.id = details.organization_id
		 LEFT JOIN inv_inventories AS inventories ON inventories.id = details.inv_inventory_id
		 LEFT JOIN inv_locations AS locations ON locations.id = details.inv_location_id
		 LEFT JOIN inv_addresses AS addresses ON addresses.id = details.inv_address_id
 WHERE details.domain_id = :domainId 