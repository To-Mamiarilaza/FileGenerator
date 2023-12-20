package models;



public class FicheLanguage {
	
	/// Field
   	
	
	@Id
	@Column(name = "id_fiche")
	Integer idFiche;
	
	@Id
	@Column(name = "id_language")
	Integer idLanguage;

	/// Constructor

    public FicheLanguage(){}

	/// Getter and setter
   	
	public Integer getIdFiche() {
	    return idFiche;
	}
	
	public void setIdFiche(Integer idFiche) {
	    this.idFiche = idFiche;
	}
	
	public Integer getIdLanguage() {
	    return idLanguage;
	}
	
	public void setIdLanguage(Integer idLanguage) {
	    this.idLanguage = idLanguage;
	}
	
}