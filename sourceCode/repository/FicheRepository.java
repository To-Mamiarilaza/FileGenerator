package repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import models.Fiche;

@Repository
public interface FicheRepository extends JpaRepository<Fiche, Integer>{

}
