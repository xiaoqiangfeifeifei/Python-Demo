
@Table(name = "inv_mat_bill_details", idStrategy = GenerationRule.UUID)
public class InvMatBillDetail {
	/**
	 * SerialVersion UID
	 */
	private static final long serialVersionUID = 495981134105362609L;

	@PrimaryKey
	@Column (name = "id", nullable = false, length = 40)
	private String id;

	@Column (name = "inv_mat_bill_head_id", length = 40)
	private String invMatBillHeadId;

	@Relation(field = "invMatBillHeadId")
	private InvMatBillHeadRef invMatBillHead;

	@Column (name = "source_no", length = 40)
	private String sourceNo;

	@Column (name = "source_line_no", length = 20)
	private String sourceLineNo;

	@Column (name = "source_type")
	private String sourceType;

	@Column (name = "material_id")
	private String materialId;

	@Relation(field = "materialId")
	private InvMaterialRef material;

	@Column (name = "qty")
	private Double qty;

	@Column (name = "process_qty")
	private Double processQty;

	@Column (name = "unit")
	private String unit;

	@Column (name = "mat_price")
	private Double matPrice;

	@Column (name = "mat_wastage_rate")
	private Double matWastageRate;

	@Column (name = "mat_rec_qty")
	private Double matRecQty;

	@Column (name = "mat_wastage_qty")
	private Double matWastageQty;

	@Column (name = "pur_qty")
	private Double purQty;

	@Column (name = "pur_price")
	private Double purPrice;

	@Column (name = "pur_unit")
	private String purUnit;

	@Column (name = "inv_cost_center_id", length = 40)
	private String invCostCenterId;

	@Relation(field = "invCostCenterId")
	private InvCostCenterRef invCostCenter;

	@Column (name = "inv_account_id", length = 40)
	private String invAccountId;

	@Relation(field = "invAccountId")
	private InvAccountRef invAccount;

	@Column (name = "organization_id", length = 40)
	private String organizationId;

	@Relation(field = "organizationId")
	private InvOrganizationRef organization;

	@Column (name = "inv_inventory_id", length = 40)
	private String invInventoryId;

	@Relation(field = "invInventoryId")
	private InvInventoryRef invInventory;

	@Column (name = "inv_location_id", length = 40)
	private String invLocationId;

	@Relation(field = "invLocationId")
	private InvLocationRef invLocation;

	@Column (name = "inv_address_id", length = 40)
	private String invAddressId;

	@Relation(field = "invAddressId")
	private InvAddressRef invAddress;

	@Column (name = "memo")
	private String memo;

	@Column (name = "lot_no")
	private String lotNo;

	@Column (name = "lock_for")
	private String lockFor;

	@Column (name = "lock_by")
	private String lockBy;

	@Column (name = "status")
	private Integer status;

	@Column (name = "create_hr_id", length = 32)
	private String createHrId;

	@Column (name = "update_hr_id", length = 32)
	private String updateHrId;
  
	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getInvMatBillHeadId() {
		return invMatBillHeadId;
	}

	public void setInvMatBillHeadId(String invMatBillHeadId) {
		this.invMatBillHeadId = invMatBillHeadId;
	}

	public InvMatBillHeadRef getInvMatBillHead() {
		return invMatBillHead;
	}

	public void setInvMatBillHead(InvMatBillHeadRef invMatBillHead) {
		this.invMatBillHead = invMatBillHead;

		if(this.invMatBillHead != null) {
			String refId = this.invMatBillHead.getId();
			if (refId != null)
				this.invMatBillHeadId = refId;
		}
	
		if(this.invMatBillHeadId == null) {
			this.invMatBillHeadId = "";
		}
	}

	public String getSourceNo() {
		return sourceNo;
	}

	public void setSourceNo(String sourceNo) {
		this.sourceNo = sourceNo;
	}

	public String getSourceLineNo() {
		return sourceLineNo;
	}

	public void setSourceLineNo(String sourceLineNo) {
		this.sourceLineNo = sourceLineNo;
	}

	public String getSourceType() {
		return sourceType;
	}

	public void setSourceType(String sourceType) {
		this.sourceType = sourceType;
	}

	public String getMaterialId() {
		return materialId;
	}

	public void setMaterialId(String materialId) {
		this.materialId = materialId;
	}

	public InvMaterialRef getMaterial() {
		return material;
	}

	public void setMaterial(InvMaterialRef material) {
		this.material = material;

		if(this.material != null) {
			String refId = this.material.getId();
			if (refId != null)
				this.materialId = refId;
		}
	
		if(this.materialId == null) {
			this.materialId = "";
		}
	}

	public Double getQty() {
		return qty;
	}

	public void setQty(Double qty) {
		this.qty = qty;
	}

	public Double getProcessQty() {
		return processQty;
	}

	public void setProcessQty(Double processQty) {
		this.processQty = processQty;
	}

	public String getUnit() {
		return unit;
	}

	public void setUnit(String unit) {
		this.unit = unit;
	}

	public Double getMatPrice() {
		return matPrice;
	}

	public void setMatPrice(Double matPrice) {
		this.matPrice = matPrice;
	}

	public Double getMatWastageRate() {
		return matWastageRate;
	}

	public void setMatWastageRate(Double matWastageRate) {
		this.matWastageRate = matWastageRate;
	}

	public Double getMatRecQty() {
		return matRecQty;
	}

	public void setMatRecQty(Double matRecQty) {
		this.matRecQty = matRecQty;
	}

	public Double getMatWastageQty() {
		return matWastageQty;
	}

	public void setMatWastageQty(Double matWastageQty) {
		this.matWastageQty = matWastageQty;
	}

	public Double getPurQty() {
		return purQty;
	}

	public void setPurQty(Double purQty) {
		this.purQty = purQty;
	}

	public Double getPurPrice() {
		return purPrice;
	}

	public void setPurPrice(Double purPrice) {
		this.purPrice = purPrice;
	}

	public String getPurUnit() {
		return purUnit;
	}

	public void setPurUnit(String purUnit) {
		this.purUnit = purUnit;
	}

	public String getInvCostCenterId() {
		return invCostCenterId;
	}

	public void setInvCostCenterId(String invCostCenterId) {
		this.invCostCenterId = invCostCenterId;
	}

	public InvCostCenterRef getInvCostCenter() {
		return invCostCenter;
	}

	public void setInvCostCenter(InvCostCenterRef invCostCenter) {
		this.invCostCenter = invCostCenter;

		if(this.invCostCenter != null) {
			String refId = this.invCostCenter.getId();
			if (refId != null)
				this.invCostCenterId = refId;
		}
	
		if(this.invCostCenterId == null) {
			this.invCostCenterId = "";
		}
	}

	public String getInvAccountId() {
		return invAccountId;
	}

	public void setInvAccountId(String invAccountId) {
		this.invAccountId = invAccountId;
	}

	public InvAccountRef getInvAccount() {
		return invAccount;
	}

	public void setInvAccount(InvAccountRef invAccount) {
		this.invAccount = invAccount;

		if(this.invAccount != null) {
			String refId = this.invAccount.getId();
			if (refId != null)
				this.invAccountId = refId;
		}
	
		if(this.invAccountId == null) {
			this.invAccountId = "";
		}
	}

	public String getOrganizationId() {
		return organizationId;
	}

	public void setOrganizationId(String organizationId) {
		this.organizationId = organizationId;
	}

	public InvOrganizationRef getOrganization() {
		return organization;
	}

	public void setOrganization(InvOrganizationRef organization) {
		this.organization = organization;

		if(this.organization != null) {
			String refId = this.organization.getId();
			if (refId != null)
				this.organizationId = refId;
		}
	
		if(this.organizationId == null) {
			this.organizationId = "";
		}
	}

	public String getInvInventoryId() {
		return invInventoryId;
	}

	public void setInvInventoryId(String invInventoryId) {
		this.invInventoryId = invInventoryId;
	}

	public InvInventoryRef getInvInventory() {
		return invInventory;
	}

	public void setInvInventory(InvInventoryRef invInventory) {
		this.invInventory = invInventory;

		if(this.invInventory != null) {
			String refId = this.invInventory.getId();
			if (refId != null)
				this.invInventoryId = refId;
		}
	
		if(this.invInventoryId == null) {
			this.invInventoryId = "";
		}
	}

	public String getInvLocationId() {
		return invLocationId;
	}

	public void setInvLocationId(String invLocationId) {
		this.invLocationId = invLocationId;
	}

	public InvLocationRef getInvLocation() {
		return invLocation;
	}

	public void setInvLocation(InvLocationRef invLocation) {
		this.invLocation = invLocation;

		if(this.invLocation != null) {
			String refId = this.invLocation.getId();
			if (refId != null)
				this.invLocationId = refId;
		}
	
		if(this.invLocationId == null) {
			this.invLocationId = "";
		}
	}

	public String getInvAddressId() {
		return invAddressId;
	}

	public void setInvAddressId(String invAddressId) {
		this.invAddressId = invAddressId;
	}

	public InvAddressRef getInvAddress() {
		return invAddress;
	}

	public void setInvAddress(InvAddressRef invAddress) {
		this.invAddress = invAddress;

		if(this.invAddress != null) {
			String refId = this.invAddress.getId();
			if (refId != null)
				this.invAddressId = refId;
		}
	
		if(this.invAddressId == null) {
			this.invAddressId = "";
		}
	}

	public String getMemo() {
		return memo;
	}

	public void setMemo(String memo) {
		this.memo = memo;
	}

	public String getLotNo() {
		return lotNo;
	}

	public void setLotNo(String lotNo) {
		this.lotNo = lotNo;
	}

	public String getLockFor() {
		return lockFor;
	}

	public void setLockFor(String lockFor) {
		this.lockFor = lockFor;
	}

	public String getLockBy() {
		return lockBy;
	}

	public void setLockBy(String lockBy) {
		this.lockBy = lockBy;
	}

	public Integer getStatus() {
		return status;
	}

	public void setStatus(Integer status) {
		this.status = status;
	}

	public String getCreateHrId() {
		return createHrId;
	}

	public void setCreateHrId(String createHrId) {
		this.createHrId = createHrId;
	}

	public String getUpdateHrId() {
		return updateHrId;
	}

	public void setUpdateHrId(String updateHrId) {
		this.updateHrId = updateHrId;
	}	
}
