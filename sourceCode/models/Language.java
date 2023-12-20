package models;



public class Language {
	
	/// Field
   	
	
	@Id
	@Column(name = "id_language")
	Integer idLanguage;
	
	@Column(name = "language_name")
	String languageName;
	
	@Column(name = "etat")
	Integer etat;

	/// Constructor

    public Language(){}

	/// Getter and setter
   	
	public Integer getIdLanguage() {
	    return idLanguage;
	}
	
	public void setIdLanguage(Integer idLanguage) {
	    this.idLanguage = idLanguage;
	}
	
	public String getLanguageName() {
	    return languageName;
	}
	
	public void setLanguageName(String languageName) {
	    this.languageName = languageName;
	}
	
	public Integer getEtat() {
	    return etat;
	}
	
	public void setEtat(Integer etat) {
	    this.etat = etat;
	}
	
}