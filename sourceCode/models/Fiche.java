package models;



public class Fiche {
	
	/// Field
   	
	
	@Id
	@Column(name = "id_fiche")
	Integer idFiche;
	
	@Column(name = "name")
	String name;
	
	@Column(name = "firstname")
	String firstname;
	
	@Column(name = "address")
	String address;
	
	@Column(name = "mail")
	String mail;
	
	@Column(name = "description")
	String description;
	
	@Column(name = "photo")
	String photo;
	
	@Column(name = "etat")
	Integer etat;

	/// Constructor

    public Fiche(){}

	/// Getter and setter
   	
	public Integer getIdFiche() {
	    return idFiche;
	}
	
	public void setIdFiche(Integer idFiche) {
	    this.idFiche = idFiche;
	}
	
	public String getName() {
	    return name;
	}
	
	public void setName(String name) {
	    this.name = name;
	}
	
	public String getFirstname() {
	    return firstname;
	}
	
	public void setFirstname(String firstname) {
	    this.firstname = firstname;
	}
	
	public String getAddress() {
	    return address;
	}
	
	public void setAddress(String address) {
	    this.address = address;
	}
	
	public String getMail() {
	    return mail;
	}
	
	public void setMail(String mail) {
	    this.mail = mail;
	}
	
	public String getDescription() {
	    return description;
	}
	
	public void setDescription(String description) {
	    this.description = description;
	}
	
	public String getPhoto() {
	    return photo;
	}
	
	public void setPhoto(String photo) {
	    this.photo = photo;
	}
	
	public Integer getEtat() {
	    return etat;
	}
	
	public void setEtat(Integer etat) {
	    this.etat = etat;
	}
	
}