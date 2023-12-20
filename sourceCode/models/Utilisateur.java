package models;



public class Utilisateur {
	
	/// Field
   	
	
	@Id
	@Column(name = "id_utilisateur")
	Integer idUtilisateur;
	
	@Column(name = "username")
	String username;
	
	@Column(name = "password")
	String password;
	
	@Column(name = "email")
	String email;
	
	@Column(name = "admin")
	Boolean admin;

	/// Constructor

    public Utilisateur(){}

	/// Getter and setter
   	
	public Integer getIdUtilisateur() {
	    return idUtilisateur;
	}
	
	public void setIdUtilisateur(Integer idUtilisateur) {
	    this.idUtilisateur = idUtilisateur;
	}
	
	public String getUsername() {
	    return username;
	}
	
	public void setUsername(String username) {
	    this.username = username;
	}
	
	public String getPassword() {
	    return password;
	}
	
	public void setPassword(String password) {
	    this.password = password;
	}
	
	public String getEmail() {
	    return email;
	}
	
	public void setEmail(String email) {
	    this.email = email;
	}
	
	public Boolean getAdmin() {
	    return admin;
	}
	
	public void setAdmin(Boolean admin) {
	    this.admin = admin;
	}
	
}